import pystray
from PIL import Image, ImageDraw, ImageFont
import requests
import threading
import time
import re

API_URL = "https://api.deadbyqueue.com/queuetime?region=eu-central-1"


def create_icon(number: str):
    size = 64
    img = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    font_size = 48
    font = None

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        try:
            font = ImageFont.truetype("Segoe UI Bold.ttf", font_size)
        except:
            font = ImageFont.load_default()

    if font != ImageFont.load_default():
        for font_size in range(48, 16, -2):
            try:
                test_font = ImageFont.truetype("arial.ttf", font_size)
            except:
                try:
                    test_font = ImageFont.truetype("Segoe UI Bold.ttf", font_size)
                except:
                    break

            bbox = draw.textbbox((0, 0), number, font=test_font)
            text_w = bbox[2] - bbox[0]
            text_h = bbox[3] - bbox[1]

            if text_w <= size - 4 and text_h <= size - 4:
                font = test_font
                break

    bbox = draw.textbbox((0, 0), number, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    x = (size - text_w) // 2
    y = (size - text_h) // 2 - bbox[1]

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            draw.text(
                (x + dx, y + dy),
                number,
                font=font,
                fill="aqua"
            )

    img = img.resize((32, 32), Image.Resampling.LANCZOS)

    return img


def fetch_queue_info():
    try:
        r = requests.get(API_URL, timeout=5)
        text = r.text.strip()
        if not text:
            return "0", "No data"

        match_minutes = re.search(r"Killer:\s*(\d+)m", text)
        minutes = match_minutes.group(1) if match_minutes else "0"

        return minutes, text
    except Exception as e:
        print("Błąd API:", e)
        return "0", "Error fetching API"


def run_tray():
    icon = pystray.Icon("DBD Queue", icon=create_icon("0"))
    icon.menu = pystray.Menu(pystray.MenuItem("Exit", lambda: icon.stop()))

    def update():
        while True:
            minutes, full_text = fetch_queue_info()
            icon.icon = create_icon(minutes)
            icon.title = full_text
            time.sleep(30)

    threading.Thread(target=update, daemon=True).start()
    icon.run()


if __name__ == "__main__":
    run_tray()