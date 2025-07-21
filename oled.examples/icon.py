import board
import busio
from PIL import Image
from adafruit_ssd1306 import SSD1306_I2C

# Setup I2C and OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = SSD1306_I2C(128, 64, i2c)

from PIL import Image, ImageDraw, ImageFont

image = Image.new("1", (128, 64))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("fontawesome-webfont.ttf", 50)
icon = "\uf2c7"  # Google FA code
font_temp=ImageFont.truetype("/home/bottle/oled/self.examples/fonts/Volter__28Goldfish_29.ttf",40)
draw.text((0, 5), icon, font=font, fill=255)
draw.text((50,14),"C",font=font_temp,fill=255)
draw.ellipse((75,15,82,22),outline=255)
oled.image(image)
oled.show()