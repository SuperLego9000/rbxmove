game="PF"

import rbxmove as rx,time,pyautogui
rx.center.start()
rx.hotkey.new('m+j', rx.game.rejoin)
rx.hotkey.new('m+l', rx.game.leave)
rx.hotkey.new('m+r', rx.game.reset)
if game=="PF":
    rx.hotkey.new('u+r', rx.press,('F5'))
    rx.hotkey.new('x',rx.press,('c'))
rx.keepalive()
