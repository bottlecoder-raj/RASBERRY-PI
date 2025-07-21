import board
import busio
import time
import sys
import termios
import tty
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

# Setup OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = SSD1306_I2C(128, 64, i2c)

# Load font and message
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
text = "  Scroll Speed Control Demo  "

# Get size of text
bbox = font.getbbox(text)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
total_width = text_width + oled.width

# Create long image
scroll_img = Image.new("1", (total_width, oled.height))
draw = ImageDraw.Draw(scroll_img)
draw.text((oled.width, (oled.height - text_height) // 2), text, font=font, fill=255)

# Setup terminal input
def get_char():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

# Initial values
x = 0
scroll_speed = 0.01

print("▶️ Press 'f' = faster, 's' = slower, 'q' = quit")

# Loop
while True:
    oled.image(scroll_img.crop((x, 0, x + oled.width, oled.height)))
    oled.show()
    time.sleep(scroll_speed)

    x += 1
    if x >= total_width - oled.width:
        x = 0

    # Check for key press (non-blocking)
    import select
    if select.select([sys.stdin], [], [], 0)[0]:
        key = get_char()
        if key == 'f':
            scroll_speed = max(0.001, scroll_speed - 0.002)
            print(f"⚡ Faster: delay = {scroll_speed:.3f}")
        elif key == 's':
            scroll_speed += 0.002
            print(f"🐢 Slower: delay = {scroll_speed:.3f}")
        elif key == 'q':
            print("🛑 Exiting...")
            break
