# Prodigy_cs_02
# Task 2 : Pixel Manipulation for Image Encryption
This project is a Python-based Image Encryption Tool that uses pixel manipulation techniques to secure images. It applies a simple XOR (Exclusive OR) operation on each pixel using a secret key to transform the image into an encrypted format.
The same process is used for decryption, making it a reversible and lossless encryption method.
# Features
- Encrypt images using XOR operation
- Decrypt images using the same key
- Key-based encryption (0–255)
- Fast and efficient pixel processing
- Supports multiple image formats (JPG, PNG)
- Simple CLI-based interface
# How It Works
  Encryption
- Convert image into pixel array
- Apply XOR operation with key
- Save encrypted image
  
Decryption
- Load encrypted image
- Apply XOR with same key
- Restore original image

 - XOR is reversible:
   - Encrypted ⊕ Key = Original
# Installation
- Install dependencies:
  ```
   pip install -r requirements.txt
   ```
# Usage
1. Run the script:
   ```
   python prodigy_cs_02.py
   ```
2. Choose an option:
   - 1: Encrypt Image
   - 2: Decrypt Image
3. Enter the path of the input image
   - The encrypted/decrypted image will be automatically saved with "_encrypted" or "_decrypted" suffix
# Author
- Created by : Suryawanshi Shravani Dnyanoba
- Task 2 : Pixel Manipulation for Image Encryption - Completed
