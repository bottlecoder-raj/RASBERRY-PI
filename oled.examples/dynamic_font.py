import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Create the OLED object (adjust for your resolution)
oled = SSD1306_I2C(128, 64, i2c)

# Clear the display
oled.fill(0)
oled.show()

# Create a blank image to draw on
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load TrueType fonts (you can change font size here)
font_small = ImageFont.truetype("/home/bottle/oled/self.examples/fonts/miscfs_.ttf", 20)
font_large = ImageFont.truetype("/home/bottle/oled/self.examples/fonts/pixelmix.ttf", 24)

# Draw text with different font sizes
draw.text((10, 0), "Small Text", font=font_small, fill=255)
draw.text((40, 30), "Large", font=font_large, fill=255)

# Show on OLED
oled.image(image)
oled.show()
