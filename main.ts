input.onButtonPressed(Button.A, function () {
	
})
basic.forever(function () {
    if (input.soundLevel() == 255) {
        music.startMelody(music.builtInMelody(Melodies.Nyan), MelodyOptions.OnceInBackground)
        for (let index = 0; index < 4; index++) {
            music.playMelody("G C5 A E B C F C5 ", 120)
        }
        servos.P2.run(68)
    }
})
