import asyncio,threading,random, time, pyautogui,os,keyboard,operator
from datetime import datetime as dt
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


class game:
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
        game.leave()
        for i in range(5):
            press('enter')
            time.sleep(0.1)

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
    def new(input:str,does,arg1=None,arg2=None,arg3=None,arg4=None,arg5=None):
        """
        Makes a new global hotkey\n
        hotkey.new('alt+x',func1) makes alt+x run func1\n
        must use keepalive() or some other method of preventing main thread from closing
        """
        if arg1==None:
            keyboard.add_hotkey(input, lambda: does())
        elif arg2==None:
            keyboard.add_hotkey(input, lambda: does(arg1))
        elif arg3==None:
            keyboard.add_hotkey(input, lambda: does(arg1,arg2))
        elif arg4==None:
            keyboard.add_hotkey(input, lambda: does(arg1,arg2,arg3))
        elif arg5==None:
            keyboard.add_hotkey(input, lambda: does(arg1,arg2,arg3,arg4))
        else:
            keyboard.add_hotkey(input, lambda: does(arg1,arg2,arg3,arg4,arg5))
    def remove(input:str):
        """
        removes the hotkey bound to input
        """
        keyboard.remove_hotkey(input)

def keepalive():
    """
    waits until the end of time
    """
    while True:
        time.sleep(9^99)

RunBool=False
class center:
    RunBool=False
    def toggle():
        """
        use this in rbxmove.hotkey.new to toggle mouse centering
        """
        global RunBool
        T = threading.Thread(target=center.center)
        RunBool=operator.not_(RunBool)
        if RunBool:
            T.start()
    def center():
        while RunBool:
            x,y=pyautogui.size()
            x,y=x/2,y/2
            try:
                pyautogui.moveTo(x,y)
            except:
                time.sleep(10)

if buildtest:
    print("rxbmove.status> built at "+ str(dt.now()))