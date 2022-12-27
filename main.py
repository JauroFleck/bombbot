from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

print("5 segundos para início do bot...")

time.sleep(5)

def click(x, y):
    
    win32api.SetCursorPos((x, y))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def findCorner(n):

    xInit = 0
    yInit = 0

    if n == 0:

        xInit = 0
        yInit = 0

    elif n == 1:

        xInit = 683
        yInit = 0

    elif n == 2:

        xInit = 0
        yInit = 384

    while 1:

        pic = pyautogui.screenshot(region=(xInit+381, yInit, 1, 384))

        #21, 15, 27
        
        for y in range(0, 384, 1):

            r,g,b = pic.getpixel((0,y))

            #print("{0} - Searching line - {1},{2},{3}".format(n,r,g,b))

            if r == 21:

                if g == 15 and b == 27:

                    #print("{0} - Found line - {1},{2},{3}".format(n,r,g,b))

                    pic = pyautogui.screenshot(region=(xInit, y+yInit, 683, 1))

                    for x in range(0,683,1):

                        r,g,b = pic.getpixel((x,0))

                        #print("{0} - Searching pixel - {1},{2},{3}".format(n,r,g,b))

                        if r == 21:

                            if r == 21 and g == 15 and b == 27:

                                #print("{0} - Found pixel ({1},{2})".format(n,xInit+x,yInit+y))

                                return (xInit+x,yInit+y)

def openHerosTab(xInit, yInit):
    
    click(xInit+161, yInit+195)
    time.sleep(0.5)
    click(xInit+161, yInit+195)

    pic = pyautogui.screenshot(region=(xInit+63,yInit+54,1,1))
    r,g,b = pic.getpixel((0,0))

    init = time.time()
    timeout = 30

    while time.time() < init+timeout:

        if r != 230 and r != 234:

            pic = pyautogui.screenshot(region=(xInit+63,yInit+54,1,1))
            r,g,b = pic.getpixel((0,0))

        else:

            return 1
    
    return 0
    
def closeHerosTab(xInit,yInit):
    
    click(xInit+179,yInit+37)
    time.sleep(0.5)
    click(xInit+179,yInit+37)
    time.sleep(1)

def checkHerosStamina(xInit,yInit):

    pyautogui.moveTo(xInit+134,yInit+167)

    for k in range(0,4,1):

        for bar in pyautogui.locateAllOnScreen('img/stamina.png', region=(xInit+83,yInit+65,41,115), grayscale=True, confidence=0.8):

            pic = pyautogui.screenshot(region=(bar.left+47, bar.top+5, 1, 1))
            r,g,b = pic.getpixel((0,0))

            if r == 70:
                
                click(bar.left+47, bar.top)
                print("GREEN STAMINA HERO: SWITCHED TO WORKING")
                time.sleep(1.5)
    
        for i in range(0,10,1):

            pyautogui.scroll(-1)

        time.sleep(0.8)
        
    for bar in pyautogui.locateAllOnScreen('img/stamina.png', region=(xInit+83,yInit+51,41,130), grayscale=True, confidence=0.8):

        pic = pyautogui.screenshot(region=(bar.left+47, bar.top+5, 1, 1))
        r,g,b = pic.getpixel((0,0))

        if r == 70:
                
            click(bar.left+47, bar.top)
            print("GREEN STAMINA HERO: SWITCHED TO WORKING")
            time.sleep(1.5)

def resetHeros(xInit,yInit):

    click(xInit+16,yInit+10)
    time.sleep(0.1)
    click(xInit+155,yInit+56)
    time.sleep(0.1)

def isPlaying(xInit,yInit):

    pic = pyautogui.screenshot(region=(xInit+125,yInit+166,1,1))
    r,g,b = pic.getpixel((0,0))

    if (r == 255 and g == 170 and b == 35) or (r == 245 and g == 163 and b == 34):

        return 0

    else:

        return 1

def connectWallet(xInit,yInit,n):

    click(xInit+125,yInit+166)
    time.sleep(5)
    init = time.time()
    timeout = 60

    if n == 1:

        while time.time() < init+timeout:

            screen = pyautogui.locateOnScreen('img/s-opera.png', region=(683,0,683,768), grayscale=True, confidence=0.9)

            if screen != None:

                pyautogui.moveTo(pyautogui.center(screen).x,pyautogui.center(screen).y)
                time.sleep(0.1)
                pyautogui.scroll(-1000)
                time.sleep(1)
                pyautogui.scroll(-1000)

                init = time.time()

                while time.time() < init+timeout:

                    button = pyautogui.locateOnScreen('img/assign-opera.png', region=(683,0,683,768), grayscale=True, confidence=0.9)

                    if button != None:

                        click(pyautogui.center(button).x,pyautogui.center(button).y)
                        return 1

                print("TIMEOUT: UNABLE TO FIND assign-opera.png")
                return 0

        print("TIMEOUT: UNABLE TO FIND s-opera.png")
        return 0
        
    else:

        while time.time() < init+timeout:

            button = pyautogui.locateOnScreen('img/assign-edge-chrome.png', region=(0,0,683,768), grayscale=True, confidence=0.9)

            if button != None:

                click(pyautogui.center(button).x,pyautogui.center(button).y)
                return 1

        print("TIMEOUT: UNABLE TO FIND assign-edge-chrome.png")
        return 0

def checkNewMap(xInit,yInit):

    button = pyautogui.locateOnScreen('img/new-map.png', region=(xInit+124,yInit+151,72,24), grayscale=True, confidence=0.9)

    if button != None:

        click(pyautogui.center(button).x, pyautogui.center(button).y)
        return 1

    else:

        return 0

def ciclePage(xInit, yInit, n):

    if checkNewMap(xInit,yInit) == 1:

        time.sleep(1)

    if count[n] < 1:

        if openHerosTab(xInit,yInit) == 0:

            pyautogui.press('f5')
            print("REFRESHING: OpenHerosTab TIMEOUT")
            time.sleep(10)

        else:
                
            checkHerosStamina(xInit,yInit)
            closeHerosTab(xInit,yInit)
            resetHeros(xInit,yInit)
            count[n] = 3

#Resolução: 1366x768
#Quadrantes:
    #Superior esquerdo  0   Chrome
    #Superior direito   1   Opera
    #Inferior esquerdo  2   Edge

#
#
#

# Antes de resetar o mapa (sair e entrar), colocar todos os heróis para descansar, esperar x segundos e resetar a fim de nao perder nenhuma bomba

#
#
#

x = [0,0,0]
y = [0,0,0]
count = [0,0,0]

print("Bot iniciado: começando busca por telas...")

for n in range(0,3,1):

    init = time.time()
    print("Buscando tela {0}...".format(n+1))
    x[n],y[n] = findCorner(n)
    print("Tela {0} encontrada ({1}ms)".format(n+1, (time.time()-init)*1000))

print("Bot inicializado com sucesso: começando primeiro ciclo.")

while 1:

    for n in range(0,3,1):
        
        if isPlaying(x[n],y[n]) == 0:

            if connectWallet(x[n],y[n],n) == 1:

                init = time.time()
                timeout = 60

                while time.time() < init+timeout:

                    pic = pyautogui.screenshot(region=(x[n]+146,y[n]+58,1,1))
                    r,g,b = pic.getpixel((0,0))

                    if r == 197 and g == 225 and b == 255:

                        click(x[n]+146,y[n]+58)
                        time.sleep(0.5)
                        timeout = 0
                        ciclePage(x[n],y[n],n)
                        break

                if timeout != 0:

                    pyautogui.press('f5')
                    time.sleep(10)
                    print("REFRESHING: LOAD PAGE TIMEOUT")

            else:

                print("TIMEOUT: UNABLE TO CONNECT WALLET {0}".format(n))

        else:

            ciclePage(x[n],y[n],n)
        
    time.sleep(120)

    for n in range(0,3,1):
        
        count[n] -= 1
