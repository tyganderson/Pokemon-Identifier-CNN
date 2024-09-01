import os

def rename_pokemon_files(root_directory):
    # Loop through all directories in the root directory
    for folder_name in os.listdir(root_directory):
        folder_path = os.path.join(root_directory, folder_name)
        
        # Check if it's actually a directory (and not a file)
        if os.path.isdir(folder_path):
            # Loop through all files in the directory
            for file_name in os.listdir(folder_path):
                # Check if the file is a jpg image
                if file_name.endswith('.jpg'):
                    # Construct the old file path
                    old_file_path = os.path.join(folder_path, file_name)
                    
                    # Get the file number from the file name
                    file_number = file_name.split('.')[0]
                    
                    # Construct the new file name
                    new_file_name = f"{folder_name}_{file_number}.jpg"
                    new_file_path = os.path.join(folder_path, new_file_name)
                    
                    # Rename the file
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed {old_file_path} to {new_file_path}")

# Example usage
root_directory = r'your_path_here'  # Change this to your actual directory
rename_pokemon_files(root_directory)
