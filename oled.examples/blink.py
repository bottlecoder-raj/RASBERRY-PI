import board
import busio
import time
import luma.oled
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

# Setup OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = SSD1306_I2C(128, 64, i2c)

# Load font
font = ImageFont.truetype("/home/bottle/oled/self.examples/fonts/pixelmix.ttf", 10)

# Blinking loop
while True:
    # 1️⃣ Draw text
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    draw.text((0, 20), "BLINKING..", font=font, fill=10)
    oled.image(image)
    oled.contrast(250)
    oled.show()
    time.sleep(0.5)  # ⏳ Visible for 0.5 seconds

    # 2️⃣ Clear screen (hide text)
    oled.fill(0)
    oled.show()
    time.sleep(0.5)  # ⏳ Off for 0.5 seconds
