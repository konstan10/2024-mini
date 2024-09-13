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
notes = [
    (494, 16),
    (988, 16),
    (740, 16),
    (622, 16),
    (988, 32),
    (740, -16),
    (622, 8),
    (523, 16),
    (1047, 16),
    (1568, 16),
    (1319, 16),
    (1047, 32),
    (1568, -16),
    (1319, 8),
    (494, 16),
    (988, 16),
    (740, 16),
    (622, 16),
    (988, 32),
    (740, -16),
    (622, 8),
    (622, 32),
    (659, 32),
    (698, 32),
    (698, 32),
    (740, 32),
    (784, 32),
    (784, 32),
    (740, 32),
    (880, 16),
    (988, 8)
]


print("Playing frequency (Hz):")

for freq, duration in notes:
    print(freq)
    playtone(freq, duration)

# Turn off the PWM
quiet()


