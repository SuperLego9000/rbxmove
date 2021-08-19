game=""

import rbxmove as rx,time,pyautogui
rx.hotkey.new('m+j', rx.game.rejoin)
rx.hotkey.new('m+l', rx.game.leave)
rx.hotkey.new('m+r', rx.game.reset)
rx.hotkey.new('alt+c',rx.center.toggle)
if game=="PF":
    rx.hotkey.remove('m+r')
    rx.hotkey.remove('m+j')
    rx.hotkey.new('m+r', rx.game.rejoin)
    rx.hotkey.new('u+r', rx.press,('F5'))
    rx.hotkey.new('z',rx.press,'c',0.01,2,0)
rx.keepalive()
