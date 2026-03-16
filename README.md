# PRODIGY_CS_02

#  Advanced Image Encryption Tool

The **Advanced Image Encryption Tool** is a desktop application built using **Python and Tkinter** that enables users to securely encrypt and decrypt images using a multi-layered encryption approach.

This project demonstrates how **image processing, cryptography concepts, and graphical interfaces** can be combined to build a secure and interactive application. The program encrypts images by applying **pixel scrambling and XOR encryption**, while the encryption key and permutation data are securely stored in an **encrypted key file protected by a password**.

The goal of this project is to provide a practical demonstration of **image security, encryption techniques, and GUI development using Python**.

---

# Project Overview

Images often contain sensitive or private information. Protecting such images from unauthorized access is important in many fields including:

- Secure file sharing
- Digital privacy
- Data protection
- Confidential image storage
- Research and educational demonstrations

This application allows users to **encrypt images so that they appear completely unreadable**, and only users with the **correct key file and password** can restore the original image.

The tool is designed with a **simple graphical interface**, making it accessible even to users with limited technical experience.

---

#  Features

- 🔐 **Secure image encryption**
- 🔓 **Image decryption with password verification**
- 🔑 **Password-protected key file generation**
- 🔀 **Pixel scrambling for visual distortion**
- ⚡ **XOR encryption for pixel data protection**
- 📁 **Automatic key file creation**
- 💻 **Graphical user interface using Tkinter**
- 🖼️ Supports **PNG, JPG, and JPEG images**
- 🛡️ Prevents unauthorized decryption
- ⚙️ Lightweight and fast processing
- 🧠 Demonstrates cryptographic concepts in Python

---

#  User Interface

The application includes a simple and clean GUI with the following components:

- Application title and description
- **Encrypt Image button**
- **Decrypt Image button**
- File selection dialogs
- Password input dialogs
- Success and error notification messages

The interface is designed to be **easy to use while maintaining strong encryption functionality**.

---

#  Encryption Architecture

The encryption system uses **multiple layers of transformation** to protect image data.

##  Pixel Scrambling

The program randomly rearranges image pixels by shuffling rows and columns using permutation arrays.

This step ensures that the image structure becomes completely distorted and visually unreadable.

Example effect:

Original Image → Structured pixels  
Scrambled Image → Random pixel distribution

---

## XOR Pixel Encryption

After scrambling, the program encrypts pixel values using a **bitwise XOR operation** with a randomly generated key.

XOR encryption modifies each pixel value using:

This operation ensures that pixel values cannot be interpreted without the correct key.

---

##  Password-Based Key Protection

The encryption key and permutation arrays are stored inside a **key file**.

Before saving, this data is encrypted using a **password-derived key** generated with **SHA-256 hashing**.

This ensures:

- The key file cannot be used without the password
- Attackers cannot easily retrieve encryption parameters
- Sensitive encryption data remains protected

---

##  Encrypted Key File

The encrypted key file contains:

- XOR encryption key
- Row permutation array
- Column permutation array

File format:
     encrypted_image.png
     encrypted_image.png.ekey.npy

Both files are required for successful decryption.

---

#  Decryption Workflow

1. Select the **encrypted image file**
2. Select the **encrypted key file**
3. Enter the **password**
4. The program decrypts the key file
5. The image is restored by reversing the encryption process

Steps performed internally:

- XOR decryption
- Pixel unscrambling
- Image reconstruction

---

#  Mathematical Concepts Used

This project demonstrates several computational concepts:

- **Permutation algorithms**
- **Bitwise XOR operations**
- **Hash functions (SHA-256)**
- **Array manipulation using NumPy**
- **Matrix-based image representation**

These techniques are widely used in **cryptography, image processing, and cybersecurity systems**.

---

# Image Processing Concepts

Digital images are represented as **multi-dimensional arrays**.


Each pixel contains three values:

- Red
- Green
- Blue

Encryption modifies these values to produce a secure encoded image.

---

#  Technologies Used

| Technology | Purpose |
|------------|--------|
| Python | Main programming language |
| Tkinter | Graphical user interface |
| NumPy | Fast numerical computations |
| Pillow (PIL) | Image processing |
| Hashlib | Password hashing |
| OS module | File handling |

---

#  Required Python Libraries

Install the required libraries using pip:

```bash
pip install pillow numpy tkinter hashlib os
