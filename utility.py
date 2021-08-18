game=""

import rbxmove as rx,time,pyautogui
rx.hotkey.new('m+j', rx.game.rejoin)
rx.hotkey.new('m+l', rx.game.leave)
rx.hotkey.new('m+r', rx.game.reset)
if game=="PF":
    rx.hotkey.new('u+r', rx.press,('F5'))
    rx.hotkey.new('x',rx.press,('c'))
    while True:
        #time.sleep(0.1)
        try:
            pyautogui.moveTo(960,540)
        except:
            time.sleep(10)
else:
    rx.keepalive()
