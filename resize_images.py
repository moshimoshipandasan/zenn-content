import os
from PIL import Image

def get_size_mb(path):
    return os.path.getsize(path) / (1024 * 1024)

def resize_image(path, target_mb=3.0):
    if get_size_mb(path) < target_mb:
        print(f"{path} is already {get_size_mb(path):.2f}MB")
        return

    img = Image.open(path)
    original_size = img.size
    
    # Resize loop
    scale = 0.9
    while True:
        new_size = (int(original_size[0] * scale), int(original_size[1] * scale))
        resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
        
        # Save to temp file to check size
        temp_path = path + ".temp"
        # Optimize=True helps for PNG
        resized_img.save(temp_path, format="PNG", optimize=True)
        
        size = get_size_mb(temp_path)
        print(f"Tried scale {scale:.2f}, size: {size:.2f}MB")
        
        if size < target_mb:
            os.replace(temp_path, path)
            print(f"Success! {path} resized to {size:.2f}MB")
            break
        
        scale -= 0.1
        if scale < 0.1:
            print(f"Failed to reduce {path} enough.")
            if os.path.exists(temp_path):
                os.remove(temp_path)
            break

files = [
    r"images\2025-11-24nanobananapro\sample-09.png",
    r"images\2025-11-24nanobananapro\sample-10.png"
]

for f in files:
    if os.path.exists(f):
        resize_image(f)
    else:
        print(f"File not found: {f}")
