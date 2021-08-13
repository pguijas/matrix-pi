#https://circuitpython.readthedocs.io/projects/neopixel/en/latest/
#https://github.com/fcambus/spleen

import board
import neopixel
import font
import time
import datetime
import math
from PIL import Image,ImageDraw,ImageFont

class Matriz:
    #Inicializamos Matriz 
    def __init__(self,height,width):
        self.pixels=neopixel.NeoPixel(board.D18,width*height)
        self.width=width
        self.height=height
        self.font_width=len(font.font[0][0])
        self.font_height=len(font.font[0])
        self.clear()

    #Manda Colores a Posiciones
    '''
    x - x - x - x - x - x - x 
    |
    |
    x - x - x - x - x - x - x 
                            |
                            |
    x - x - x - x - x - x - x 
    |
    |
    x - x - x - x - x - x - x 
                            |
                            |
    x - x - x - x - x - x - x 
    '''
    def send(self,x,y,c):
        if y%2==0: #par
            real_x=x
        else:      #impar (invertimos)
            real_x=self.width-1-x 
        self.pixels[self.width*y+real_x]=c

    def send_all(self,c):
        self.pixels.fill(c)

    def clear(self):
        self.pixels.fill((0,0,0))

    def send_text(self,text,c):
        
        print("Pendiente desarrollo")

        '''
        if text_width>self.width:
            
        else:
        ''' 
            

    #esto usa las matrices
    def print_char(self,char,color,offset_x=0,offset_y=0):
        char_matrix=font.font[ord(char)-33]
        for y in range(self.font_height):
            for x in range(self.font_width):
                if char_matrix[y][x]==1:
                    self.send(x+offset_x,y+offset_y,color)
              
                #Mejor dejar fondo transparente
                #else:
                #   self.send(x+offset_x,y+offset_y,(0,0,0))

    def print_center(self,text,color=(0,50,0),margin=0):
        self.clear()
        tamano=len(text)*(self.font_width+margin)-margin
        print(tamano)
        if tamano>self.width:
            print("error, sobrepasa ancho, no se puede centrar >" + str(self.width))
        else:
            print("Sin hacer")
            i=math.trunc((self.width-tamano)/2)
            print(i)
            for c in text:
                print(c)
                self.print_char(c,color,offset_x=i)
                i=i+self.font_width+margin



matriz = Matriz(8,32)
matriz.print_center("10:00")
