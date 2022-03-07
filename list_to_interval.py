import numpy as np

def intervals(data):

    data = sorted(list(set(data)))

    A = np.array(data)

    #input list moved by one element backward,
    #one zero added to the end to make it
    #the same size
    a = np.array(data[1:] + [0])

    diff = a - A #the difference to the next element

    #lists with start and end point,
    #the first one is moved by one with the start
    #point being the first element
    s, e = [data[0]], []

    for (i,n) in enumerate(diff):
        if n != 1: #if the difference is greater than 1
            #the next start point is in the size of the leap
            s.append(data[i] + n)
            #this end point is located in the same place in the input list
            e.append(data[i])
            
    #cutting of the last start point
    #(it is the zero we added) 
    intervals = list(zip(s[:-1], e)) 
    out = []
    out = [f'{i[0]} - {i[1]}' if i[0] != i[1] else f'{i[0]}' for i in intervals]

    return ', '.join(out)