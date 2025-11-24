import os
from PIL import Image

file_path = r"c:\Users\moshi\MyProjects\blog\zenn-content\images\2025-11-24nanobananapro\sample-08.png"
max_size = 3 * 1024 * 1024  # 3MB

def resize_single_image(path):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return

    if os.path.getsize(path) <= max_size:
        print(f"Skipping {path} (already under 3MB)")
        return

    print(f"Processing {path}...")
    try:
        with Image.open(path) as img:
            fmt = img.format
            scale = 1.0
            
            while True:
                scale *= 0.9
                new_width = int(img.width * scale)
                new_height = int(img.height * scale)
                
                resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                temp_path = path + ".temp"
                resized_img.save(temp_path, format=fmt, optimize=True)
                
                if os.path.getsize(temp_path) <= max_size:
                    break
                
                if scale < 0.1:
                    print(f"Could not reduce {path} below 3MB even with significant resizing.")
                    if os.path.exists(temp_path):
                        os.remove(temp_path)
                    return

        if os.path.exists(path + ".temp"):
             os.replace(path + ".temp", path)
             print(f"Resized {path} to {os.path.getsize(path)} bytes")

    except Exception as e:
        print(f"Error processing {path}: {e}")
        if os.path.exists(path + ".temp"):
            os.remove(path + ".temp")

if __name__ == "__main__":
    resize_single_image(file_path)
