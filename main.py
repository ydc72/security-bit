def security1(start: bool):
    if start:
        pass
    else:
        servos.P2.run(-81)

def on_button_pressed_a():
    music.start_melody(music.built_in_melody(Melodies.NYAN),
        MelodyOptions.ONCE_IN_BACKGROUND)
    for index in range(4):
        music.play_melody("G C5 A E B C F C5 ", 120)
    servos.P2.run(68)
input.on_button_pressed(Button.A, on_button_pressed_a)

servos.P2.set_stop_on_neutral(True)