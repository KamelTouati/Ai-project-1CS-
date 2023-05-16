from subprocess import call

def build(*args):
    call(['python', 'build.py'])

build()