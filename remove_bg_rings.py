from PIL import Image
import os

def remove_white_bg(path):
    try:
        img = Image.open(path)
        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            # Tuned threshold to catch grayish whites in sketches while preserving light pinks
            if item[0] > 230 and item[1] > 230 and item[2] > 230:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)
        img.save(path, "PNG")
        print(f"Processed {path}")
    except Exception as e:
        print(f"Error processing {path}: {e}")

remove_white_bg('assets/images/wedding_rings_sketch.png')
