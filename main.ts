input.onButtonPressed(Button.A, function () {
    current_random = (multiplier * current_random + adder) % modulus
    basic.showNumber(current_random % max_value)
})
let current_random = 0
let max_value = 0
let adder = 0
let multiplier = 0
let modulus = 0
modulus = 5891
multiplier = 1763
adder = 2565
max_value = 10
current_random = 371
basic.showNumber(current_random % max_value)
