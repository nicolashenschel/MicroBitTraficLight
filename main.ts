input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 10; index++) {
        pins.digitalWritePin(DigitalPin.P0, 1)
        basic.pause(PauseTid)
        pins.digitalWritePin(DigitalPin.P0, 0)
        pins.digitalWritePin(DigitalPin.P2, 1)
        basic.pause(PauseTid)
        pins.digitalWritePin(DigitalPin.P2, 0)
        pins.digitalWritePin(DigitalPin.P1, 1)
        basic.pause(PauseTid)
        pins.digitalWritePin(DigitalPin.P1, 0)
    }
})
input.onButtonPressed(Button.AB, function () {
    PauseTid = 500
})
input.onButtonPressed(Button.B, function () {
    PauseTid += 500
})
let PauseTid = 0
PauseTid = 500
basic.forever(function () {
    basic.showNumber(PauseTid / 100)
})
