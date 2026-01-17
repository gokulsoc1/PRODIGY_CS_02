import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image
import numpy as np
import hashlib
import os
"""
  you want to dounload proper package.
  i already check it code will be prefect working.
  if any issue update pip packages or dounload pip packages.
"""

# ================== CRYPTO UTILITIES ==================

def password_to_key(password):
    return hashlib.sha256(password.encode()).digest()[0]


def scramble_pixels(img, seed):
    np.random.seed(seed)
    h, w, _ = img.shape
    row_perm = np.random.permutation(h)
    col_perm = np.random.permutation(w)
    scrambled = img[row_perm][:, col_perm]
    return scrambled, row_perm, col_perm


def unscramble_pixels(img, row_perm, col_perm):
    inv_row = np.argsort(row_perm)
    inv_col = np.argsort(col_perm)
    restored = img[inv_row][:, inv_col]
    return restored


# ================== KEY FILE ENCRYPTION ==================

def encrypt_key_file(key, row_perm, col_perm, password, path):
    pw_key = password_to_key(password)

    data = np.concatenate((
        np.array([key], dtype=np.uint16),
        row_perm.astype(np.uint16),
        col_perm.astype(np.uint16)
    ))

    encrypted = data ^ pw_key
    np.save(path, encrypted)


def decrypt_key_file(password, path, h, w):
    pw_key = password_to_key(password)
    encrypted = np.load(path)
    decrypted = encrypted ^ pw_key

    key = int(decrypted[0])
    row_perm = decrypted[1:1 + h]
    col_perm = decrypted[1 + h:1 + h + w]

    return key, row_perm, col_perm


# ================== ENCRYPT IMAGE ==================

def encrypt_image():
    img_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    if not img_path:
        return

    password = simpledialog.askstring(
        "Password", "Set password for key file:", show="*"
    )
    if not password:
        return

    img = Image.open(img_path).convert("RGB")
    img_array = np.array(img)

    key = np.random.randint(1, 255)

    scrambled, row_perm, col_perm = scramble_pixels(img_array, key)
    encrypted_img = scrambled ^ key

    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Files", "*.png")]
    )

    if save_path:
        Image.fromarray(encrypted_img.astype("uint8")).save(save_path)

        encrypt_key_file(
            key,
            row_perm,
            col_perm,
            password,
            save_path + ".ekey.npy"
        )

        messagebox.showinfo(
            "Success",
            "Image encrypted successfully!\nEncrypted key file created."
        )


# ================== DECRYPT IMAGE ==================

def decrypt_image():
    enc_path = filedialog.askopenfilename(
        title="Select Encrypted Image",
        filetypes=[("PNG Files", "*.png")]
    )
    if not enc_path:
        return

    key_path = filedialog.askopenfilename(
        title="Select Encrypted Key File",
        filetypes=[("Encrypted Key", "*.ekey.npy")]
    )
    if not key_path:
        return

    password = simpledialog.askstring(
        "Password", "Enter key password:", show="*"
    )
    if not password:
        return

    img = Image.open(enc_path).convert("RGB")
    img_array = np.array(img)
    h, w, _ = img_array.shape

    try:
        key, row_perm, col_perm = decrypt_key_file(
            password, key_path, h, w
        )
    except Exception:
        messagebox.showerror("Error", "Wrong password or corrupted key file!")
        return

    decrypted = img_array ^ key
    original = unscramble_pixels(decrypted, row_perm, col_perm)

    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Files", "*.png")]
    )

    if save_path:
        Image.fromarray(original.astype("uint8")).save(save_path)
        messagebox.showinfo("Success", "Image decrypted successfully!")


# ================== GUI ==================

root = tk.Tk()
root.title("Advanced Image Encryption Tool")
root.geometry("460x330")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

tk.Label(
    root,
    text="🔐 Advanced Image Encryption",
    font=("Segoe UI", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
).pack(pady=20)

frame = tk.Frame(root, bg="#2b2b3d", bd=2, relief="ridge")
frame.pack(padx=20, pady=10, fill="both", expand=True)

tk.Label(
    frame,
    text="Pixel Scrambling + XOR + Encrypted Key File",
    bg="#2b2b3d",
    fg="#cccccc",
    font=("Segoe UI", 10)
).pack(pady=15)

tk.Button(
    frame,
    text="Encrypt Image",
    width=24,
    font=("Segoe UI", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    relief="flat",
    command=encrypt_image
).pack(pady=10)

tk.Button(
    frame,
    text="Decrypt Image",
    width=24,
    font=("Segoe UI", 11, "bold"),
    bg="#2196F3",
    fg="white",
    relief="flat",
    command=decrypt_image
).pack(pady=10)

root.mainloop()