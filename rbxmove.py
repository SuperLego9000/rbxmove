import asyncio,threading,random, time, pyautogui,os,keyboard
from datetime import datetime as dt
from asyncio.tasks import wait
IKnowWhatImDoing = False
if IKnowWhatImDoing == False:
    if os.name != 'nt':  # check for windows 10
        if os.name != 'dos':
            print("not windows 10")
            raise OSError("OS is not windows")
        else:
            print("please use windows 10")

buildtest = True


class Async:#all of my Async functions
    """
    All Async functions in one place\n
    Only use these inside rbxmove.Async.Run
    """
    async def move(key:str, studs:int, speed:int=16):
        """
        move('w',9,16)\n would move 9 studs forward becuase speed is 16

        press key for studs/speed

        runs asynchronously
        """
        if studs <= 0:
            raise ValueError("studs can not be smaller than or equal to 0")
        pyautogui.keyDown(key)
        await asyncio.sleep(studs/speed)
        pyautogui.keyUp(key)

    async def turn(direction:str, angle:int, player:bool=False):
        """
        turn('left',90)\n
        turns left 90 degrees

        direction can only be left or right

        runs asynchronously
        """
        if direction.lower() != 'left' and direction.lower() != 'right':
                raise ValueError(f"{direction} is not a valid direction")
        if player:
            for i in range(10):
                pyautogui.scroll(10, False, True)
                i -= 1
        pyautogui.keyDown(direction)
        await asyncio.sleep(angle/90*.665)
        pyautogui.keyUp(direction)
        if player:
            for i in range(5):
                pyautogui.scroll(-10, False, True)
                i -= 1

    async def press(key:str, duration:float=0.01, repitition:int=1, interval:int=0):
        """presses key for duration every interval for repitition\n
        allowed keys are the same as pyautogui's

        runs asynchronously
        """
        for i in range(repitition):
            pyautogui.keyDown(key)
            await asyncio.sleep(duration)
            pyautogui.keyUp(key)
            await asyncio.sleep(interval)
            i -= 1
    
    def Run(func:list):
        """
        runs all the rbxmove.Async functions

        ex:    rbxmove.Async.Run([\n
            rbxmove.Async.move('w',9),\n
            rbxmove.Async.press('space'),\n
            rbxmove.Async.turn('left',90)\n
            ])
        """
        asyncio.run(__1__(func))
    #end class Async

def move(key:str, studs:int, speed:int=16):
    """
    move('w',9,16)\n would move 9 studs forward becuase speed is 16
    press key for studs/speed
    """
    if studs <= 0:
        raise ValueError("studs can not be smaller than or equal to 0")
    pyautogui.keyDown(key)
    time.sleep(studs/speed)
    pyautogui.keyUp(key)

def turn(direction:str, angle:int, player:bool=False):
    """
    turn('left',90)\n
    turns left 90 degrees

    direction can only be left or right
    """
    if direction.lower() != 'left' and direction.lower() != 'right':
            raise ValueError(f"{direction} is not a valid direction")
    if player:
        for i in range(10):
            pyautogui.scroll(10, False, True)
            i -= 1
    pyautogui.keyDown(direction)
    time.sleep(angle/90*.665)
    pyautogui.keyUp(direction)
    if player:
        for i in range(5):
            pyautogui.scroll(-10, False, True)
            i -= 1

def press(key:str,duration:float=0.01,repitition:int=1,interval:int=0):
    """presses key for duration every interval for repitition\n
    allowed keys are the same as pyautogui's
    """
    for i in range(repitition):
        pyautogui.keyDown(key)
        time.sleep(duration)
        pyautogui.keyUp(key)
        time.sleep(interval)
        i-=1

def align(zoomout:int=-10):
    """
    Zooms in then out to align player with camera
    """
    if type(zoomout)!=int:
        raise   TypeError(f"{zoomout} is not an integer")
    for i in range(10):
        pyautogui.scroll(10,False,True)
        i-=1
    for i in range(2):
        pyautogui.scroll(zoomout,False,True)
        i-=1

def chat(message:str,repitition:int=1,interval:int=0,chatcooldown:bool=True,maxchatsbeforwait:int=8,send:bool=True):
    """
    puts message inside roblox chat

    message must be string
    """
    if type(message)!=str:
        raise TypeError(f"{message} is not a string")
    if chatcooldown:
        chated=0
    for i in range(repitition):
        if chatcooldown:
            chated+=1
            if chated==maxchatsbeforwait:
                if repitition!=maxchatsbeforwait:
                    time.sleep(12)
                    chated=0
        pyautogui.press('/')
        pyautogui.typewrite(message)
        time.sleep(.1)
        if send:
            pyautogui.press('enter')
        if  repitition>1:
            time.sleep(interval)
        i-=1

def countto(countto:int,interval:int=1):
    """
    waits for count to finish
    """
    
    for i in range(countto):
        print(i+1,"/",countto)
        i-=1
        time.sleep(interval)

def consoleclear(lines:int=50):
    """
    Spams the console with newlines
    """
    if type(lines)!=int:
        raise TypeError(f"variable \'lines\' must be int; currently {type(lines)}")
    for i in range(lines):
        print("\n")
    
def donothing():
    """
    does nothing
    """
    pass

def leave(lastchat:str=None,delay:float=0.01):
    """
    leaves the game and optionaly says some goodbyes
    
    there is a chance that roblox currently could have a bug where the menu doesn\'t reconize rbxmove trying to leave,
    \nif that is the case; change the delay higher,\n
    switch from windows store version to web version or vice versa,\n
    or don\'t use this function, sorry for the inconvenience
    """
    if lastchat!=None:
        chat(message=lastchat)
    pyautogui.press('esc')
    time.sleep(delay)
    pyautogui.press('l')
    time.sleep(delay)
    pyautogui.press('enter')
def rejoin(delay:float=5):
    """
    trys to rejoin the game\n
    delay is converted into milliseconds
    """
    leave()
   #time.sleep(delay)
    for i in range(5):
        press('enter')
        time.sleep(.1)

def reset(lastchat:str=None,delay:float=0.01):
    """
    resets and optionaly says some last words
    
    there is a chance that roblox currently could have a bug where the menu doesn\'t reconize rbxmove trying to reset,
    \nif that is the case; change the delay higher,\n
    switch from windows store version to web version or vice versa,\n
    or don\'t use this function, sorry for the inconvenience
    """
    if lastchat!=None:
        chat(message=lastchat)
    pyautogui.press('esc')
    time.sleep(delay)
    pyautogui.press('r')
    time.sleep(delay)
    pyautogui.press('enter')

def waitfor(waitfor:bool,interval:float=0.2):
    """
    attempts to  wait for a bool to be True
    """
    if type(waitfor)==bool:
        while waitfor!=True:
            time.sleep(interval)
    else:
        raise TypeError("value not bool")

async def __1__(args):
        """
        dont run this function
        """
        if type(args)!=list:
            raise TypeError("args is not a list")
        if(wait):
            try:
                await asyncio.gather(*args)
            except TypeError:
                pass

def cw(string:str):
    """
    writes to the console
    """
    try:
        print(f"rbxmove.console> {string}")
    except:
        print("rbxmove.status> cw failed")

class hotkey:
    """
    all hotkey functions in rbxmove
    """
    def new(input:str,does,args=None):
        """
        Makes a new global hotkey\n
        hotkey.new('alt+x',func1) makes alt+x run func1\n
        hotkey.new('alt'+'x',func1) makes pressing alt then x run func1\n
        must use keepalive() or some other method of preventing main thread from closing
        """
        keyboard.add_hotkey(input, lambda: does(args))
    def remove_all():
        """
        unregisters all hotkeys
        """
        keyboard.remove_all_hotkeys()

def keepalive():
    while True:
        donothing()

if buildtest:
    print("rxbmove.status> built at "+ str(dt.now()))