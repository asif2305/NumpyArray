# creation numpy array
import numpy as np 

#Creating a rank 1 Array
arr=np.array([1,2,3])
print("Array with rank 1 : \n",arr)

#Creating a rank 2 Array
arr=np.array([[1,2,3],
             [4,5,6]])
print("Array with rank 2 : \n",arr)

# Creating array with tuple

arr= np.array((1,2,3))
print("\n Array creating with tuple :\n",arr)

"""output...............

Array with Rank 1: 
 [1 2 3]
Array with Rank 2: 
 [[1 2 3]
 [4 5 6]]

Array creating with tuple:
 [1 3 2]
"""
