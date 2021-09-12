import numpy as np


def te_to_ccm(myte):
    te =[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
    
    te_matrix = np.array([ [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
     [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
     [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
     [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
     [[5, 5, 5], [5, 5, 5], [5, 5, 5]],
     [[6, 6, 6], [6, 6, 6], [6, 6, 6]],
     [[7, 7, 7], [7, 7, 7], [7, 7, 7]],
     [[8, 8, 8], [8, 8, 8], [8, 8, 8]],
     [[9, 9, 9], [9, 9, 9], [9, 9, 9]] ])
    
    
    if(myte < te[0]):
        my_matrix = te_matrix[0]
    elif(myte > te[8]):
        my_matrix = te_matrix[8]
    else:
        for i in range(len(te)):
            if(te[i] > myte):
                g = (myte - te[i-1])/(te[i] - te[i-1])
                my_matrix = g*te_matrix[i] + (1-g)*te_matrix[i-1]          
                break
    
    return my_matrix


            
if __name__ == '__main__':
    myte =  8120.0
    my_matrix =  te_to_ccm(myte)
    print(my_matrix)
    





