import rbxmove as rx,time,pyautogui
game=pyautogui.confirm("Game?","RBX Utils",["PF","Standard"])

if game=="PF":
    rx.hotkey.remove('m+r')
    rx.hotkey.remove('m+j')
    rx.hotkey.new('m+r', rx.game.rejoin)
    rx.hotkey.new('u+r', rx.press,('F5'))
    rx.hotkey.new('z',rx.press,'c',0.01,2,0)
else:
    rx.hotkey.new('m+j', rx.game.rejoin)
    rx.hotkey.new('m+l', rx.game.leave)
    rx.hotkey.new('m+r', rx.game.reset)
    rx.hotkey.new('alt+c',rx.center.toggle)
rx.keepalive()