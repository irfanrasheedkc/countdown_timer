#import the time module
import time

#define the coountdown function
def countdown(t):
    while t:
        mins, secs=divmod(t,60) #convert seconds into minutes and second
        timer='{:02d}:{:02d}'.format(mins,secs)
        print('\r', timer, end='')
        time.sleep(1)
        t-=1
    print('\nTimes up!!!')

#input time in seconds
t=input('Enter time in seconds: ')
#function call
countdown(int(t))