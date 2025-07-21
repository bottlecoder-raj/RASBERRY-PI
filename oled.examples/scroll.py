import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont
import time

# Initialize I2C and OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = SSD1306_I2C(128, 64, i2c)

# Load font (make sure this path is valid!)
font = ImageFont.truetype("/home/bottle/oled/self.examples/fonts/pixelmix.ttf", 16)

# Your scrolling message
text = "  OLED Bidirectional Scroll Demo  "

# Calculate text width and height
bbox = font.getbbox(text)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Create a wider image for scrolling
scroll_img = Image.new("1", (text_width, oled.height))
draw = ImageDraw.Draw(scroll_img)

# Draw text centered vertically in the scroll image
draw.text((0, (oled.height - text_height) // 2), text, font=font, fill=255)

# Bidirectional scrolling loop
try:
    while True:
        # Scroll Left
        for x in range(0, text_width - oled.width + 1, 2):
            oled.image(scroll_img.crop((x, 0, x + oled.width, oled.height)))
            oled.show()
            time.sleep(0.005)

        # Scroll Right
        for x in reversed(range(0, text_width - oled.width + 1, 2)):
            oled.image(scroll_img.crop((x, 0, x + oled.width, oled.height)))
            oled.show()
            time.sleep(0.005)

except KeyboardInterrupt:
    oled.fill(0)
    oled.show()
    print("Scroll stopped.")
