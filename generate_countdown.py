from datetime import datetime, timezone
from PIL import Image, ImageDraw, ImageFont
import os

# Countdown target: October 10th, 17:00 Madrid
target = datetime(2015, 10, 10, 17, 0, 0, tzinfo=ZoneInfo("Europe/Madrid"))
now = datetime.now(ZoneInfo("Europe/Madrid"))
diff = target - now

days = diff.days
hours, remainder = divmod(diff.seconds, 3600)
minutes = remainder // 60

# New format: 7D:12H:30m
countdown_text = f"{days}D:{hours}H:{minutes}m"

# Image settings
width, height = 600, 200
text_color = (255, 255, 255, 255) # White (with alpha)
font_size = 72
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" # Ubuntu font

# Create transparent image
image = Image.new("RGBA", (width, height), (0, 0, 0, 0)) # RGBA, alpha=0 for transparent
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font_path, font_size)
bbox = font.getbbox(countdown_text)
text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
position = ((width - text_width) // 2, (height - text_height) // 2)
draw.text(position, countdown_text, fill=text_color, font=font)

# Ensure /image exists
os.makedirs("image", exist_ok=True)
image.save("image/countdown.png")
