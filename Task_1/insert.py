import numpy as np
from util import data_file

def randomInsert(file):
    arr = np.reshape(np.random.randint(0, 10000, 10000, dtype=int), (10, -1))
    with open(file, 'a') as f:
        for part in arr:
            f.write(','.join(map(str, part)))
            f.write('\n')

def fileRead(file):
    with open(file, 'r') as f:
        for line in f:
            print(len(line.split(',')))
        

if __name__=='__main__':
    randomInsert(data_file)
    fileRead(data_file)
