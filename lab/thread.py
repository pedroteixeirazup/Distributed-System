'''
    Created by: Pedro Henrique Faria Teixeira
    For: Distributed System Class        
'''


import threading
import time
import random
import string

aux = -1
upperMsg = ''
upperLetter = ''
flag = False

def generate_string(length=80):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))


msg = generate_string()
print('Lower string: ' + msg)
def worker(message, increment):
    global upperMsg
    global upperLetter
    if len(message) > len(upperMsg):
        if message[increment].islower():
            upperLetter=message[increment].upper()
            upperMsg+=upperLetter
            global aux
            aux = increment
    else: 
        global flag
        flag = True

    # print(upperLetter)
    time.sleep(0.2)

t = [0]*30

while flag == False:
    for i in range(30):
        t[i] = threading.Thread(target=worker,args=(msg, aux+1))
        t[i].start()
        t[i].join()


print('Upper string: ' + upperMsg)


# Reason of I can't restart a thread in python
# https://stackoverflow.com/questions/29692250/restarting-a-thread-in-python
