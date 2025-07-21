import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont
import time

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Create OLED object (128x64 resolution)
oled = SSD1306_I2C(128, 64, i2c)

# Clear display
oled.fill(0)
oled.show()

# Create blank image and drawing canvas
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load a font
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)

# Draw text
draw.text((10, 20), "Brightness Test", font=font, fill=255)

# Display the image
oled.image(image)
oled.show()

# 🌓 Cycle through different contrast levels
for contrast in [10, 50, 100, 150, 200, 255,10]:
    oled.set_contrast(contrast)
    print(f"Contrast set to: {contrast}")
    time.sleep(1)

# Optional: Reset contrast to normal
oled.set_contrast(255)
