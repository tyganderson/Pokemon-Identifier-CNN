from PIL import Image
import os

def resize_images(root_directory, size=(128, 128)):
    # Loop through all directories and files in the root directory
    for folder_name in os.listdir(root_directory):
        folder_path = os.path.join(root_directory, folder_name)
        
        # Check if it's a directory
        if os.path.isdir(folder_path):
            # Loop through all files in the directory
            for file_name in os.listdir(folder_path):
                if file_name.endswith('.jpg'):
                    # Construct the full file path
                    file_path = os.path.join(folder_path, file_name)
                    
                    # Open the image
                    try:
                        with Image.open(file_path) as img:
                            # Resize the image using LANCZOS (formerly ANTIALIAS)
                            img = img.resize(size, Image.Resampling.LANCZOS)
                            
                            # Save the image, overwriting the original
                            img.save(file_path)
                            print(f"Resized {file_path}")
                    except Exception as e:
                        print(f"Error resizing {file_path}: {e}")

# Example usage
root_directory = r'your_path_here'  # Change this to your actual directory path
resize_images(root_directory)
