import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw
from PIL import ImageFont

# Initialize I2C and OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = SSD1306_I2C(128, 64, i2c)

# Clear the screen
oled.fill(0)
oled.show()
font_large = ImageFont.truetype("/home/bottle/oled/self.examples/fonts/pixelmix.ttf", 24)

img = Image.new("1", (128, 64), color=0)
draw = ImageDraw.Draw(img)
draw.ellipse((20, 10, 100, 60), outline=255)  # Head
draw.ellipse((40, 25, 48, 33), fill=255)      # Left eye
draw.ellipse((72, 25, 80, 33), fill=255)      # Right eye
draw.arc((45, 35, 75, 55), start=0, end=180, fill=255)  # Smile

oled.image(img)
oled.show()
