import board
import busio
import time
from PIL import Image, ImageDraw
import adafruit_ssd1306

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear display
oled.fill(0)
oled.show()

# Create image buffer
width = oled.width
height = oled.height
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)

# Ball properties
ball_radius = 10
x, y = 10, 10
vx, vy = 2, 2  # velocity

try:
    while True:
        # Clear buffer
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        # Draw ball
        draw.ellipse((x - ball_radius, y - ball_radius, x + ball_radius, y + ball_radius), fill=255)
        
        # Send buffer to OLED
        oled.image(image)
        oled.show()

        # Update position
        x += vx
        y += vy

        # Bounce off edges
        if x - ball_radius <= 0 or x + ball_radius >= width:
            vx = -vx
        if y - ball_radius <= 0 or y + ball_radius >= height:
            vy = -vy

        # Delay for animation smoothness
        time.sleep(0.001)

except KeyboardInterrupt:
    oled.fill(0)
    oled.show()
    print("Animation stopped.")
