import board
import busio
import time
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

# Initialize I2C and OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = SSD1306_I2C(128, 64, i2c)

# Load font and prepare message
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
text = " Scroll + Fade + Blink Demo   "

# Measure text size
bbox = font.getbbox(text)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
total_width = text_width + oled.width

# Create a scrollable image
scroll_img = Image.new("1", (total_width, oled.height))
draw = ImageDraw.Draw(scroll_img)
draw.text((oled.width, (oled.height - text_height) // 2), text, font=font, fill=255)

# Add set_contrast() to your SSD1306 driver if missing:
# def set_contrast(self, contrast):
#     self.write_cmd(0x81)
#     self.write_cmd(contrast & 0xFF)

# Main loop
x = 0
blink = True

while True:
    # ⚙️ Scrolling text
    window = scroll_img.crop((x, 0, x + oled.width, oled.height))
    oled.image(window)
    oled.show()

    # 🌗 Fade in & out (adjust contrast)
    for contrast in list(range(0, 256, 15)) + list(range(255, -1, -15)):
        oled.set_contrast(contrast)
        time.sleep(0.005)

    time.sleep(0.1)  # Scroll delay
    x += 1
    if x >= total_width - oled.width:
        x = 0
        # ✨ Blink after a full scroll
        if blink:
            oled.fill(0)
            oled.show()
            time.sleep(0.1)
            oled.image(window)
            oled.show()
            time.sleep(0.1)
