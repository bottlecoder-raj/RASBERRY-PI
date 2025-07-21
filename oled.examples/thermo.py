import board
import busio
from PIL import Image
from adafruit_ssd1306 import SSD1306_I2C
from time import sleep

# Setup I2C and OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = SSD1306_I2C(128, 64, i2c)

from PIL import Image, ImageDraw, ImageFont
font = ImageFont.truetype("fontawesome-webfont.ttf", 50)
font_temp=ImageFont.truetype("/home/bottle/oled/self.examples/fonts/C&C Red Alert [INET].ttf",40)

try:
    while True:
        image = Image.new("1", (128, 64))
        draw = ImageDraw.Draw(image)
        icon1 = "\uf2cb"  # TEMP 0
        icon2 = "\uf2ca"  # temp 1
        icon3 = "\uf2c9"  # temp 2
        icon5 = "\uf2c7"  # temp 3
        icon4 = "\uf2c8"
        draw.text((0, 5), icon1, font=font, fill=255)
        draw.text((50,14),"C",font=font_temp,fill=255)
        draw.ellipse((75,15,82,22),outline=255)
        oled.image(image)
        oled.show()
        sleep(0.5)
        draw.text((0, 5), icon2, font=font, fill=255)
        draw.text((50,14),"C",font=font_temp,fill=255)
        draw.ellipse((75,15,82,22),outline=255)
        oled.image(image)
        oled.show()
        sleep(0.5)
        draw.text((0, 5), icon3, font=font, fill=255)
        draw.text((50,14),"C",font=font_temp,fill=255)
        draw.ellipse((75,15,82,22),outline=255)
        oled.image(image)
        oled.show()
        sleep(0.5)
        draw.text((0, 5), icon4, font=font, fill=255)
        draw.text((50,14),"C",font=font_temp,fill=255)
        draw.ellipse((75,15,82,22),outline=255)
        oled.image(image)
        oled.show()
        sleep(0.5)
        draw.text((0, 5), icon5, font=font, fill=255)
        draw.text((50,14),"C",font=font_temp,fill=255)
        draw.ellipse((75,15,82,22),outline=255)
        oled.image(image)
        oled.show()
        sleep(0.5)
     
      
except KeyboardInterrupt:
    print("Animation STOPPED")
    oled.fill(0)
    oled.show()