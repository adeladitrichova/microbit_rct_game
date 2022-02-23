pins.touchSetMode(TouchTarget.P1, TouchTargetMode.Capacitive)
pins.touchSetMode(TouchTarget.P2, TouchTargetMode.Capacitive)
let is_pin1 = input.pinIsPressed(TouchPin.P1)
let is_pin2 = input.pinIsPressed(TouchPin.P2)
let player1 = false
let player2 = false
let start = false
let show = false
let cheater1 = false
let cheater2 = false
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    
    player1 = true
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    
    player2 = true
})
forever(function cast_hry() {
    
    basic.clearScreen()
    basic.pause(randint(3000, 10000))
    show = true
    start = true
    music.playMelody("C", 120)
    while (start == true && player1 == false && player2 == false) {
        basic.showIcon(IconNames.Yes)
    }
    pause(3000)
})
forever(function vyhodnocovani() {
    
    if (start == false && player1 == true) {
        cheater1 = true
    } else if (start == false && player2 == true) {
        cheater2 = true
    } else if (start == true && cheater1 == true && cheater2 == true) {
        basic.showString("C")
        restart()
    } else if (start == true && cheater1 == true) {
        basic.showString("B")
        restart()
    } else if (start == true && cheater2 == true) {
        basic.showString("A")
        restart()
    } else if (start == true && player1 == true) {
        basic.showString("1")
        restart()
    } else if (start == true && player2 == true) {
        basic.showString("2")
        restart()
    } else if (start == true && player1 == true && player2 == true) {
        basic.showString("R")
        restart()
    }
    
})
function restart() {
    
    start = false
    player1 = false
    player2 = false
    cheater1 = false
    cheater2 = false
    basic.clearScreen()
}

