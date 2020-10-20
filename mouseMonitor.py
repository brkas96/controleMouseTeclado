from pynput.mouse import Button, Listener

#https://www.youtube.com/watch?v=eK7p1e8-6jU

def click(x,y,button, pressed):
    print(x, y, button, pressed)
    if not pressed:
        return False

def move(x,y):
    print(x,y)

#listener = Listener(on_click=click, on_move=move, on_scroll=scroll) #Monitora o mouse

#listener= Listener(on_click=click)
#listener.start()
#listener.join()
#listener.stop()

with Listener(on_click=click, on_move=move) as listener:
    listener.join()



