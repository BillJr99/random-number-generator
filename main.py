def on_button_pressed_a():
    global current_random
    current_random = (multiplier * current_random + adder) % modulus
    basic.show_number(current_random % max_value)
input.on_button_pressed(Button.A, on_button_pressed_a)

current_random = 0
max_value = 0
adder = 0
multiplier = 0
modulus = 0
seed = 371
modulus = 5891
multiplier = 1763
adder = 2565
max_value = 10
current_random = seed
basic.show_number(current_random % max_value)