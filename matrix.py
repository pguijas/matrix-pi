#https://circuitpython.readthedocs.io/projects/neopixel/en/latest/
#https://github.com/fcambus/spleen

import board
import neopixel
import font
import time
import datetime
from PIL import Image,ImageDraw,ImageFont

class Matriz:
    #Inicializamos Matriz 
    def __init__(self,width,height):
        self.pixels=neopixel.NeoPixel(board.D18,width*height)
        self.width=width
        self.height=height
        
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
        if x%2==0: #par
            real_y=y
        else:      #impar (invertimos)
            real_y=self.height-1-y 
        self.pixels[self.height*x+real_y]=c

    def send_all(self,c):
        self.pixels.fill(c)

    def send_text(self,text,c):
        
        print("Pendiente desarrollo")

        '''
        if text_width>self.width:
            
        else:
        ''' 
            

    #esto usa las matrices
    def print_char(self,char,color,offset_x=0,offset_y=0):
        char_matrix=font.font[ord(char)-33]
        for x in range(len(char_matrix)):
            for y in range(len(char_matrix[0])):
                if font[char][x][y]==1:
                    self.send(x+offset_x,y+offset_y,color)
                else:
                    self.send(x+offset_x,y+offset_y,(0,0,0))

    def send_hour(self,h1,h2,m1,m2,c):
        self.print_char(h1,c,1,6)
        self.print_char(h2,c,1,10)
        self.print_char(m1,c,1,15)
        self.print_char(m2,c,1,19)

matriz = Matriz(8,32)
matriz.send_all((0,0,1))
#matriz.send_hour(1,2,0,0,(0,50,0))