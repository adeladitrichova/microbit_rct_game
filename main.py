pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
pins.touch_set_mode(TouchTarget.P2, TouchTargetMode.CAPACITIVE)

is_pin1 = input.pin_is_pressed(TouchPin.P1)
is_pin2 = input.pin_is_pressed(TouchPin.P2)

player1 = False
player2 = False
start = False
show = False
cheater1 = False
cheater2 = False

def on_pin_pressed_p1():

    global player1

    player1 = True
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_pin_pressed_p2():

    global player2

    player2 = True
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def cast_hry():

    global start, player1, player2, show

    basic.clear_screen()
    basic.pause(randint(3000, 10000))
    show = True
    start = True
    music.play_melody("C", 120)

    while start == True and player1 == False and player2 == False:
        basic.show_icon(IconNames.YES)
    pause(3000)

forever(cast_hry)

def vyhodnocovani():

    global start, player1, player2, cheater1, cheater2
    
    if start == False and player1 == True:
        cheater1 = True
    
    elif start == False and player2 ==  True:
            cheater2 = True


    elif start == True and cheater1 == True and cheater2 == True:
        basic.show_string("C")
        restart()

    elif start == True and cheater1 == True:
        basic.show_string("B")
        restart()

    elif start == True and cheater2 == True:
        basic.show_string("A")
        restart()

    elif start == True and player1 == True:
        basic.show_string("1")
        restart()

    elif start == True and player2 == True:
        basic.show_string("2")
        restart()

    elif start == True and player1 == True and player2 == True:
        basic.show_string("R")
        restart()

forever(vyhodnocovani)

def restart():

    global player1, player2, start, cheater1, cheater2

    start = False
    player1 = False
    player2 = False
    cheater1 = False
    cheater2 = False
    basic.clear_screen()