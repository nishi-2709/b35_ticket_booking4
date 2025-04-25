from PIL import Image, ImageDraw, ImageFont
import os

# Create a 400x300 image with a light gray background
img = Image.new('RGB', (400, 300), color=(240, 240, 240))
draw = ImageDraw.Draw(img)

# Add a border
draw.rectangle([(0, 0), (399, 299)], outline=(200, 200, 200))

# Add text
try:
    font = ImageFont.truetype("arial.ttf", 30)
except IOError:
    font = ImageFont.load_default()

text = "No Image Available"
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

x = (400 - text_width) // 2
y = (300 - text_height) // 2

draw.text((x, y), text, fill=(150, 150, 150), font=font)

# Save the image
os.makedirs('static/images', exist_ok=True)
img.save('static/images/default-show.jpg', 'JPEG') 