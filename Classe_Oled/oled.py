import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306



class Exibição:
    
    def __init__(self, texto):
        
        self.texto = texto

    def exibe_oled(self):
        
        
        text = self.texto

        oled_reset = digitalio.DigitalInOut(board.D4)
        WIDTH = 128
        HEIGHT = 64  # Change to 64 if needed
        BORDER = 5
        i2c = board.I2C()
        oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)
        oled.fill(0)
        oled.show()
         
        image = Image.new("1", (oled.width, oled.height))
        draw = ImageDraw.Draw(image)
         
        draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)
         
        draw.rectangle((BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1), outline=0,fill=0,)
         
        font = ImageFont.load_default()

        (font_width, font_height) = font.getsize(text)
        draw.text(
            (oled.width // 2 - font_width // 3, oled.height // 5 - font_height // 3),
            text,
            font=font,
            fill=255,
        )
         
        oled.image(image)
        oled.show()










#thiago = Exibição("thiago")
#thiago.exibe_oled()





































