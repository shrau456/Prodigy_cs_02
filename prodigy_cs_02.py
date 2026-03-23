from PIL import Image
import numpy as np
import os

class ImageEncryptor:
    def __init__(self, key):
        self.key = key

    def generate_output_path(self, input_path, is_encrypt=True):
        """Generate output path based on input path."""
        base, ext = os.path.splitext(input_path)
        if is_encrypt:
            return f"{base}_encrypted{ext}"
        else:
            return f"{base}_decrypted{ext}"

    def encrypt_image(self, input_path, output_path=None):
        """Encrypt an image by applying XOR operation with the key to each pixel."""
        try:
            # Generate output path if not provided
            if output_path is None:
                output_path = self.generate_output_path(input_path, True)
            
            # Open the image
            img = Image.open(input_path)
            # Convert to RGB if not already
            img = img.convert('RGB')
            
            # Convert image to numpy array
            img_array = np.array(img)
            
            # Apply XOR operation to each pixel with the key
            encrypted_array = img_array ^ self.key
            
            # Create new image from encrypted array
            encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
            
            # Save the encrypted image
            encrypted_img.save(output_path)
            print(f"Image encrypted successfully and saved to {output_path}")
            
        except Exception as e:
            print(f"Error during encryption: {str(e)}")

    def decrypt_image(self, input_path, output_path=None):
        """Decrypt an image by applying XOR operation with the key to each pixel."""
        try:
            # Generate output path if not provided
            if output_path is None:
                output_path = self.generate_output_path(input_path, False)
            
            # Open the encrypted image
            img = Image.open(input_path)
            
            # Convert image to numpy array
            img_array = np.array(img)
            
            # Apply XOR operation to each pixel with the key
            decrypted_array = img_array ^ self.key
            
            # Create new image from decrypted array
            decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
            
            # Save the decrypted image
            decrypted_img.save(output_path)
            print(f"Image decrypted successfully and saved to {output_path}")
            
        except Exception as e:
            print(f"Error during decryption: {str(e)}")

def main():
    # Example usage
    key = 0x55  # Simple key (can be any value between 0-255)
    encryptor = ImageEncryptor(key)
    
    # Get user input
    print("Image Encryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Enter your choice (1 or 2): ")
    
    input_path = input("Enter the path of the input image: ")
    
    if choice == "1":
        encryptor.encrypt_image(input_path)
    elif choice == "2":
        encryptor.decrypt_image(input_path)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()