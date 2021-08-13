# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:05:24 2018

@author: HIMANSHU
"""

######## Mouse Controls ##############
import os
from PIL import ImageOps
from PIL import ImageGrab
import time
import win32api, win32con
from numpy import *
import cv2

x=345
y=280
def screenGrab():
    im = ImageGrab.grab((x,y,x+795,y+585))
    im.save(os.getcwd() + '\\full_snap_' + str(int(time.time())) + '.png','PNG')
    return im 

########### Mouse Controls ############

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print('Click.')
    
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print('Left Down')
    
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print('Left release')
    
def mousePos(cord):
    win32api.SetCursorPos((cord[0], cord[1]))
    
def get_cords():
    x,y = win32api.GetCursorPos()
    print(x,y)
    
########### Navigate Through Start Menu########    

def StartGame():
    # Click on Play Button
    mousePos((576,431))
    leftClick()
    time.sleep(1)

    # Click on Continue Button
    mousePos((627,621))
    leftClick()
    time.sleep(1)

    # Click on Skip Button
    mousePos((831,678))
    leftClick()
    time.sleep(1)

    # Click on Continue Button
    mousePos((638,606))
    leftClick()
    time.sleep(1)
    
########## Cordinate Class ########

class Cord:
    f_rice=(361,558)
    f_nori=(310,614)
    f_roe=(369,614)
    
    foldMat=(450,638)
    
    phone=(842,602)
    
    menu_toppings=(798,494)
    t_nori=(768,510)
    t_roe=(850,507)
    t_exit=(830,553)
    
    
    menu_rice=(808,519)
    buy_rice=(812,512)
    
    delivery_norm=(635,509)
    
    
#### Keep Track of Ingredients####
foodOnHand = {'rice':10,'nori':10,'roe':10}

########## Making Sush ################
def makeFood(food):
    if food == 'caliroll':
        print('Making a california roll')
        foodOnHand['rice']=1
        foodOnHand['nori']=1
        foodOnHand['roe']=1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.foldMat)
        leftClick()
        time.sleep(1.5)
        
    elif food == 'onigiri':
        print('Making a california roll')
        foodOnHand['rice']=2
        foodOnHand['nori']=1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.foldMat)
        leftClick()
        time.sleep(1.5)
        
    elif food == 'gunkan':
        print('Making a california roll')
        foodOnHand['rice']=1
        foodOnHand['nori']=1
        foodOnHand['roe']=2
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.foldMat)
        leftClick()
        time.sleep(1.5)
        
        
        
######  Buy Food/Navigation    Phone Menu ##### 

def buyFood(food):
    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.1)
        leftClick()
        s = screenGrab()
        print('test')
        time.sleep(.1)
        if s.getpixel((Cord.buy_rice[0]-x,Cord.buy_rice[1]-y)) != (255,255,255):
            print('rice is available')
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print('rice is not available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(.1)
            buyFood(food)
         
    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.1)
        leftClick()
        s = screenGrab()
        print('test')
        time.sleep(.1)
        if s.getpixel((Cord.t_nori[0]-x,Cord.t_nori[1]-y)) != (88, 68, 57):
            print('nori is available')
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print('nori is not available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.1)
        leftClick()
        s = screenGrab()
        print('test')
        time.sleep(.1)
        if s.getpixel((Cord.t_roe[0]-x,Cord.t_roe[1]-y)) != (88, 68, 57):
            print('roe is available')
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['roe'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print('roe is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(.1)
            buyFood(food)
            
######### Clearing Tables ########
def clear_tables():
    mousePos((430, 540))
    leftClick()
     
    mousePos((560, 540))
    leftClick()
        
    mousePos((685, 540))
    leftClick()
       
    mousePos((810, 540))
    leftClick()
      
    mousePos((935, 540))
    leftClick()
        
    mousePos((1060, 540))
    leftClick()
    time.sleep(1)
                
     
####### Setting New Bounding Boxes  ####
def get_seat_one():
    box = (398,352,427,376)
    #box = (396,352,428,376)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a= array(im.getcolors())
    a= a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png','PNG')
    return a

def get_seat_two():
    # box = (524,352,553,376)
    box = (524,352,553,376)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a= array(im.getcolors())
    a= a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png','PNG')
    return a

def get_seat_three():
    box = (650,352,679,376)
    #box = (650,352,680,376)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a= array(im.getcolors())
    a= a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png','PNG')
    return a

def get_seat_four():
    box = (776,352,805,376)
    #box = (776,352,806,376)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a= array(im.getcolors())
    a= a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png','PNG')
    return a

def get_seat_five():
    box = (902,352,931,376)
    #box = (902,352,933,376)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a= array(im.getcolors())
    a= a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png','PNG')
    return a

def get_seat_six():
    box = (1028,352,1057,376)
    # box = (1028,352,1059,376)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a= array(im.getcolors())
    a= a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png','PNG')
    return a


############# Sushi Types Dictionary ##########
sushiTypes = {1532:'onigiri',2176:'caliroll',1284:'gunkan'}

############# Checking Food on Hand   ###########
def checkFood():
    for i,j in foodOnHand.items():
        if i == 'nori' or i =='rice' or i=='roe':
            if j<=4:
                print('%s is low and needs to be replenished'%i)
                buyFood(i)


########### Putting It All Together ##### Final Flow ######
#Check seats > if customer, make order > check food > if low.
# buy food > clear tables > repeat

def check_customer():
    s1=get_seat_one()
    if s1 in sushiTypes:
        print('table 1 is occupied and needs %s'%sushiTypes[s1])
        makeFood(sushiTypes[s1])
    else:
        print('sushi not found!\n sushiType =%i'%s1)
    
    s2=get_seat_two()
    if s2 in sushiTypes:
        print('table 2 is occupied and needs %s'%sushiTypes[s2])
        makeFood(sushiTypes[s2])
    else:
        print('sushi not found!\n sushiType =%i'%s2)
    
    s3=get_seat_three()
    if s3 in sushiTypes:
        print('table 3 is occupied and needs %s'%sushiTypes[s3])
        makeFood(sushiTypes[s3])
    else:
        print('sushi not found!\n sushiType =%i'%s3)
    
    s4=get_seat_four()
    if s4 in sushiTypes:
        print('table 4 is occupied and needs %s'%sushiTypes[s4])
        makeFood(sushiTypes[s4])
    else:
        print('sushi not found!\n sushiType =%i'%s4)
    
    s5=get_seat_five()
    if s5 in sushiTypes:
        print('table 5 is occupied and needs %s'%sushiTypes[s5])
        makeFood(sushiTypes[s5])
    else:
        print('sushi not found!\n sushiType =%i'%s5)
    
    s6=get_seat_six()
    if s6 in sushiTypes:
        print('table 6 is occupied and needs %s'%sushiTypes[s6])
        makeFood(sushiTypes[s6])
    else:
        print('sushi not found!\n sushiType =%i'%s6)
    
    clear_tables()
    checkFood()
 
    
##### MAIN FUNCTION #######
    
def main():
    StartGame()
    while True:
        check_customer()     
        if cv2.waitKey(1) == ord('q'):
            break;