import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont
import time

# Setup OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = SSD1306_I2C(128, 64, i2c)

# Clear screen
oled.fill(0)
oled.show()

# Create an image to draw on
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load font and draw text
font = ImageFont.truetype("//home/bottle/oled/self.examples/fonts/ProggyTiny.ttf",40)
draw.text((10, 20), "Fading...", font=font, fill=255)

# Show the static image
oled.image(image)
oled.show()

# 🌀 Fade loop
while True:
    # Fade in
    for contrast in range(0, 256, 5):
        oled.set_contrast(contrast)
        time.sleep(0.1)

    # Fade out
    for contrast in range(255, -1, -5):
        oled.set_contrast(contrast)
        time.sleep(0.1)
