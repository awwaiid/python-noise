"""
Let's brush up on some python by making some noise!
"""

import pyaudio
import math
import struct

# Must use floats!
time_step = 1.0 / 48000.0

def play(gen):
    p = pyaudio.PyAudio()

    # open stream
    stream = p.open(
        format = pyaudio.paFloat32,
        channels = 1,
        rate = 48000,
        output = True)

    while True:
        buffer = ''
        for i in range(100):
            sample = gen.next()
            if sample == None:
                break
            buffer += struct.pack("f",sample)
        if buffer != "":
            stream.write(buffer)
        else:
            return None

def none_to_zero(v):
    return 0 if v == None else v

def sine( freq = 440 ):
    global time_step
    t = 0.0
    while True:
        t += time_step
        yield math.sin( 2 * 3.1415 * t * freq )

def combine( gens = [] ):
    while True:
        sum = 0
        for i in gens:
            sum += none_to_zero(i.next())
        yield sum

""" Play some gens one after another, in a sequence """
def sequence( gens = [] ):
    for gen in gens:
        sample = gen.next()
        while sample != None:
            yield sample
            sample = gen.next()

# gen = sine( freq = 220 )
# gen = combine( gens = [sine( freq = 220 ), sine( freq = 440)] )

# gen = sequence( gens = [
    # combine( gens = [sine( freq = 220 ), sine( freq = 440)] ),
    # combine( gens = [sine( freq = 440 ), sine( freq = 880)] )
# ])

gen = combine( gens = [
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 220 ),
  sine( freq = 440)
] )

play( gen = gen )

