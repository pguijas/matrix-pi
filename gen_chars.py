import numpy as np
import time
import datetime
from PIL import Image,ImageDraw,ImageFont
import sys

def char_to_pixels(text, path='fonts/5x8.ttf', w=5, h=7, fontsize=8):
    font = ImageFont.truetype(path, fontsize) 
    wc, hc = font.getsize(text)  
    #h *= 2 
    image = Image.new('L', (wc, hc), 0)  
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, fill="white", font=font) 
    #image.show()
    arr = np.asarray(image)
    return arr[(hc-h):hc,0:w] #recortamos para que sea del formato requerido (recorta desde la esquina inferior izquierda)

def for_all_chars():
    original_stdout = sys.stdout
    with open('font.py', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print('#array starts at the 33º ascii character (!)')
        print('font = [')
        for n in range(33,126): #[33, 126] los que son para mi los caracteres "básicos"
            if chr(n).isprintable():
                matr_str="["
                for row in char_to_pixels(chr(n), fontsize=8):
                    matr_str=matr_str+" ["
                    for item in row:
                        if item>0:
                            matr_str=matr_str+" 1,"
                        else:
                            matr_str=matr_str+" 0,"
                    matr_str=matr_str[0:-1]
                    matr_str=matr_str+" ],"
                
                print("\t" + matr_str[0:-1]+"],")
        print(']')
        sys.stdout = original_stdout

