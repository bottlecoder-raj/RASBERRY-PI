import board
import busio
from PIL import Image
from adafruit_ssd1306 import SSD1306_I2C
import time

# Setup OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = SSD1306_I2C(128, 64, i2c)

# Load the PNG and prepare layers
logo = Image.open("images/pi_logo.png").convert("RGBA")
white_bg = Image.new("RGBA", logo.size, (255, 255, 255, 255))
posn = ((oled.width - logo.width) // 2, (oled.height - logo.height) // 2)

while True:
    for angle in range(0, 360, 10):
        rotated = logo.rotate(angle, resample=Image.BILINEAR)
        combined = Image.composite(rotated, white_bg, rotated)

        # Make final image to send (convert to 1-bit)
        frame = Image.new("1", (oled.width, oled.height), 0)
        frame.paste(combined.convert("1"), posn)

        oled.image(frame)
        oled.show()
        time.sleep(0.05)
