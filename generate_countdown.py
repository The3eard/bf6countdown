from datetime import datetime, timezone
from PIL import Image, ImageDraw, ImageFont
import os

# Countdown target: October 10th, 00:00 UTC
target = datetime(2025, 10, 10, 0, 0, 0, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
diff = target - now

days = diff.days
hours, remainder = divmod(diff.seconds, 3600)
minutes = remainder // 60

countdown_text = f"{days} days, {hours} hours, {minutes} minutes left"

# Image settings
width, height = 600, 200
bg_color = (30, 30, 30)
text_color = (255, 255, 255)
font_size = 48
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" # Change if needed

# Create image
image = Image.new("RGB", (width, height), bg_color)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font_path, font_size)
text_width, text_height = draw.textsize(countdown_text, font=font)
position = ((width - text_width) // 2, (height - text_height) // 2)
draw.text(position, countdown_text, fill=text_color, font=font)

# Ensure /image exists
os.makedirs("image", exist_ok=True)
image.save("image/countdown.png")
