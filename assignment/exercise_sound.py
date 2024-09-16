#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)

# How fast to play the song
freq: float = 30
duration: float = 0.1  # seconds
# Creating notes in order to play a song with well defined keys
 (494, 16),  # B4, sixteenth note
    (988, 16),  # B5, sixteenth note
    (740, 16),  # F#5, sixteenth note
    (622, 16),  # D#5, sixteenth note
    (988, 32),  # B5, thirty-second note
    (740, -16), # F#5, staccato sixteenth note (short and detached)
    (622, 8),   # D#5, eighth note
    (523, 16),  # C5, sixteenth note
    (1047, 16), # C6, sixteenth note
    (1568, 16), # G6, sixteenth note
    (1319, 16), # E6, sixteenth note
    (1047, 32), # C6, thirty-second note
    (1568, -16),# G6, staccato sixteenth note (short and detached)
    (1319, 8),  # E6, eighth note
    (494, 16),  # B4, sixteenth note
    (988, 16),  # B5, sixteenth note
    (740, 16),  # F#5, sixteenth note
    (622, 16),  # D#5, sixteenth note
    (988, 32),  # B5, thirty-second note
    (740, -16), # F#5, staccato sixteenth note (short and detached)
    (622, 8),   # D#5, eighth note
    (622, 32),  # D#5, thirty-second note
    (659, 32),  # E5, thirty-second note
    (698, 32),  # F5, thirty-second note
    (698, 32),  # F5, thirty-second note
    (740, 32),  # F#5, thirty-second note
    (784, 32),  # G5, thirty-second note
    (784, 32),  # G5, thirty-second note
    (740, 32),  # F#5, thirty-second note
    (880, 16),  # A5, sixteenth note
    (988, 8)    # B5, eighth note


print("Playing frequency (Hz):")

for freq, duration in notes:
    print(freq)
    playtone(freq, duration)

# Turn off the PWM
quiet()


