import math

def square_root(x):
    y = math.sqrt(x)
    return y
# function to server
def put_in_string(pos,x):
    
    if(x == 'X' or x == 'O'):
        return pos + x + ' '

    print('try again')  
    return ''

#function for the client
def mount_tabu():
    with open('data.txt', 'r') as f:
        data = f.read()
        data_aux = data.split(' ')

        if len(data_aux) <= 9:
            return data_aux
        else:
            return 'FISNIHED'

#function for the client
def recuper_tabu(arr):
    arr_tabu = [0]*9
    for i in arr:
        if i == '1X':
            arr_tabu[0] = 'X'
        elif i == '2X':
            arr_tabu[1] = 'X'
        elif i == '3X':
            arr_tabu[2] = 'X'
        elif i == '4X':
            arr_tabu[3] = 'X'
        elif i == '5X':
            arr_tabu[4] = 'X'
        elif i == '6X':
            arr_tabu[5] = 'X'
        elif i == '7X':
            arr_tabu[6] = 'X'
        elif i == '8X':
            arr_tabu[7] = 'X'
        elif i == '9X':
            arr_tabu[8] = 'X'
        elif i == '1O':
            arr_tabu[0] = 'O'
        elif i == '2O':
            arr_tabu[1] = 'O'
        elif i == '3O':
            arr_tabu[2] = 'O'
        elif i == '4O':
            arr_tabu[3] = 'O'
        elif i == '5O':
            arr_tabu[4] = 'O'
        elif i == '6O':
            arr_tabu[5] = 'O'
        elif i == '7O':
            arr_tabu[6] = 'O'
        elif i == '8O':
            arr_tabu[7] = 'O'
        elif i == '9O':
            arr_tabu[8] = 'O'
    return arr_tabu