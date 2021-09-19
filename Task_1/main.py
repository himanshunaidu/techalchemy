import os

from quickSort import sort
from heap import buildHeap, heapify, heappush, heappop, AugmentedEntry
from util import data_dir, data_file, final_data_file

#Divide 10 GB of data into 10 parts and sort each part and save
def sortParts(file, dir):
    with open(file, 'r') as f:
        part = 0
        for line in f:
            line = list(map(int, line.split(',')))
            sort(line)
            data_file, part = os.path.join(dir, 'data'+str(part)), part+1
            with open(data_file, 'w+') as fa:
                f_data = ','.join(map(str, line))
                print(len(f_data))
                fa.write(f_data)
    return part+1

#Use heap sort logic to merge the 10 parts into one single file
def sortAll(dir, final_file, numFiles):
    dataset, indices = extractDataset(dir, final_file, numFiles)

    heap = []
    #Store first 10 elements
    for i in range(numFiles):
        heappush(heap, AugmentedEntry(dataset[i][indices[i]], i))
    
    while len(heap)>0:
        val = heappop(heap)
        newVal = getNext(dataset, indices, val.lindex)
        if newVal is None: continue
        heappush(heap, AugmentedEntry(newVal, val.lindex))
        with open(final_file, 'a') as ff:
            ff.write(str(val.value)+',')
    # print(res)
            

#Dataset extraction can be optimized to make sure that only subsets of the intermediate data files are present in memory
#Due to the high complexity of the file handling code to do so, we will ignore that for now
def extractDataset(dir, final_file, numFiles):
    dataset, indices = [], [0 for _ in range(numFiles)] 
    for i in range(numFiles):
        filename = os.path.join(dir,'data'+str(i))
        with open(filename, 'r') as fr:
            dataset.append(list(map(int, fr.readline().split(','))))
    return dataset, indices

#Get next logic can be optimized to make sure that the entire data part need not be in memory to get the next element
#Due to the high complexity of the file handling code to do so, we will ignore that for now
def getNext(dataset, indices, part):
    indices[part] = indices[part]+1
    if indices[part] == len(dataset[part]): return None
    return dataset[part][indices[part]]

if __name__=='__main__':
    # numFiles = sortParts(data_file, data_dir)
    # extractDataset(data_dir, final_data_file, 10)
    sortAll(data_dir, final_data_file, 10)
