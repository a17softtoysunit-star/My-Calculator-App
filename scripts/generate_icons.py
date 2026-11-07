import os
from PIL import Image, ImageDraw

ICON_SPECS = {
    "ldpi": 36,
    "mdpi": 48,
    "hdpi": 72,
    "xhdpi": 96,
    "xxhdpi": 144,
    "xxxhdpi": 192
}

BASE_SIZE = 512

def create_base_calculator_icon():
    img = Image.new("RGBA", (BASE_SIZE, BASE_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Base container
    bg_color = (24, 26, 32, 255)
    corner_radius = 110
    draw.rounded_rectangle(
        [(16, 16), (BASE_SIZE - 16, BASE_SIZE - 16)],
        radius=corner_radius,
        fill=bg_color
    )
    draw.rounded_rectangle(
        [(16, 16), (BASE_SIZE - 16, BASE_SIZE - 16)],
        radius=corner_radius,
        outline=(50, 55, 65, 255),
        width=4
    )

    # Screen display bar
    draw.rounded_rectangle(
        [(64, 60), (BASE_SIZE - 64, 150)],
        radius=20,
        fill=(15, 16, 20, 255),
        outline=(40, 44, 52, 255),
        width=3
    )
    draw.rounded_rectangle(
        [(BASE_SIZE - 140, 95), (BASE_SIZE - 85, 115)],
        radius=6,
        fill=(0, 122, 255, 255)
    )

    # 4 Grid Keys (+, -, x, =)
    keys = [
        {"rect": [(64, 180), (230, 310)], "color": (45, 48, 58, 255), "type": "plus"},
        {"rect": [(282, 180), (448, 310)], "color": (45, 48, 58, 255), "type": "minus"},
        {"rect": [(64, 340), (230, 448)], "color": (45, 48, 58, 255), "type": "multiply"},
        {"rect": [(282, 340), (448, 448)], "color": (255, 159, 10, 255), "type": "equals"}
    ]

    for k in keys:
        draw.rounded_rectangle(k["rect"], radius=24, fill=k["color"])
        x1, y1 = k["rect"][0]
        x2, y2 = k["rect"][1]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if k["type"] == "plus":
            draw.rectangle([(cx - 24, cy - 5), (cx + 24, cy + 5)], fill=(255, 255, 255, 255))
            draw.rectangle([(cx - 5, cy - 24), (cx + 5, cy + 24)], fill=(255, 255, 255, 255))
        elif k["type"] == "minus":
            draw.rectangle([(cx - 24, cy - 5), (cx + 24, cy + 5)], fill=(255, 255, 255, 255))
        elif k["type"] == "multiply":
            d = 18
            draw.line([(cx - d, cy - d), (cx + d, cy + d)], fill=(255, 255, 255, 255), width=6)
            draw.line([(cx + d, cy - d), (cx - d, cy + d)], fill=(255, 255, 255, 255), width=6)
        elif k["type"] == "equals":
            draw.rectangle([(cx - 24, cy - 14), (cx + 24, cy - 6)], fill=(255, 255, 255, 255))
            draw.rectangle([(cx - 24, cy + 6), (cx + 24, cy + 14)], fill=(255, 255, 255, 255))

    return img

def generate_all_icons(output_dir="res/icon/android"):
    os.makedirs(output_dir, exist_ok=True)
    master_icon = create_base_calculator_icon()
    master_path = os.path.join(output_dir, "icon-512.png")
    master_icon.save(master_path, "PNG")

    for density, size in ICON_SPECS.items():
        resized = master_icon.resize((size, size), Image.Resampling.LANCZOS)
        filepath = os.path.join(output_dir, f"icon-{density}.png")
        resized.save(filepath, "PNG")

if __name__ == "__main__":
    generate_all_icons()
  
