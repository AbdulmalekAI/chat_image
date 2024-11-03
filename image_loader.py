# Here we load the image from folder images 
# Path of the image is "/home/abdulmalek-alsalmi/Desktop/SA/the_project/images/"
# %%
# هذا هو الكود الخاص بتحميل الصور من المجلد images
from PIL import Image
import webbrowser
import os

 
def load_image_from_folder(image_name):
    folder_path = "/home/abdalmi/Desktop/SA/the_project/images/"
    # Ensure to try both .png and .jpg
    image_path_options = [
        os.path.join(folder_path, image_name + ".png"),
        os.path.join(folder_path, image_name + ".jpg")
    ]
    for file_path in image_path_options:
        if os.path.exists(file_path):
            try:
                with Image.open(file_path) as img:
                    temp_path = "/tmp/temp_image.png"  # Change path as needed for other OSes
                    img.save(temp_path)  # Save as PNG or any other browser-supported format
                    webbrowser.open(f"file://{temp_path}")
                    return file_path  # Return the file path instead of the image object
            except (IOError, OSError):
                print(f"Image {file_path} is not a valid image.")
    print(f"Image {image_name} not found in specified formats.")
    return None


