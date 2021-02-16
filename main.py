def on_button_pressed_a():
    for index in range(10):
        pins.digital_write_pin(DigitalPin.P0, 1)
        basic.pause(PauseTid)
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P2, 1)
        basic.pause(PauseTid)
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.digital_write_pin(DigitalPin.P1, 1)
        basic.pause(PauseTid)
        pins.digital_write_pin(DigitalPin.P1, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global PauseTid
    PauseTid = 500
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global PauseTid
    PauseTid += 500
input.on_button_pressed(Button.B, on_button_pressed_b)

PauseTid = 0
PauseTid = 500

def on_forever():
    basic.show_number(PauseTid / 100)
basic.forever(on_forever)
