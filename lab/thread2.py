import threading
import time
import random
import string



def generate_string(length=80):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))

sem = threading.Semaphore()
string = generate_string()
counter = 0
stringAuxAux = ''
def worker(index):
    global string
    global counter
    global sem 
    global stringAuxAux
    # print(string)
    stringAux = ''
    flag = True
    # print('Thread: ' + str(index))
    while flag:
        if index  == counter:
            sem.acquire()
            for letters in string:
                if letters.islower():
                    stringAux+=letters.upper()
                    print(stringAux)
                    counter = (counter + 1) % 30
                if len(stringAux) == len(string) and stringAux.isupper():
                    flag = False
            sem.release()
            time.sleep(1)
        
        stringAuxAux = stringAux


def main():
    global string
    global stringAuxAux

    print(string)
    # time.sleep(5)
    t = [0]*30
    for i in range(30):
        # print(i)
        t[i] = threading.Thread(target=worker,args=(i, ))
        t[i].start()
        

    for i in range(30):
        t[i].join()
    
    print('Upper String: ' + stringAuxAux)

if __name__ == "__main__":
    main() 