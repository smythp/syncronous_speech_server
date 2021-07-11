import rpyc
from subprocess import call

def speak(text_to_speak, speed=270):
    call(["espeak",f"-s{speed} -ven+18 -z",text_to_speak])


def speak_synchronous(text):
    '''If the server is running, add text to the speech queue to be read aloud synchronously.'''


    c = rpyc.connect("localhost", 18861)

    c.root.remote_speak(text)

