from PIL import Image
import os

def remove_white_bg(path):
    try:
        img = Image.open(path)
        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            # Change all white (also shades of whites) to transparent
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)
        img.save(path, "PNG")
        print(f"Processed {path}")
    except Exception as e:
        print(f"Error processing {path}: {e}")

remove_white_bg('assets/images/heart_balloons_pink.png')
remove_white_bg('assets/images/bunting_flags_pink.png')
