import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

# Create I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Create OLED display object (128x64 or 128x32)
oled = SSD1306_I2C(128, 64, i2c)

# Clear display
oled.fill(0)
oled.show()

# Create blank image for drawing
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load a font
font = ImageFont.load_default()

# Draw text
draw.text((0, 0), "Hello, OLED!", font=font, fill=150)

# Display image on OLED
oled.image(image)
oled.show()
