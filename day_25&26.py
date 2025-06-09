import numpy as np

# # a = np.array([1, 2, 3])                 # 1D array
# b = np.array([[1, 2], [3, 4]]) 

# # print("1D Array:", a)
# # print("2D Array:\n", b)


# # # properties of arrays
# # print("shape of 1D array:",a.shape)
# # print("shape of 2D array:", b.shape)
# # print("size of 1D array:", a.size)
# # print("size of 2D array:", b.size)
# # print("number of dimensions :" ,a.ndim)
# # print("number of dimensions :" ,b.ndim)


# # # mathematical operations
# # x=np.array([1, 2, 3])
# # y=np.array([4, 5, 6])
# # print(x+y)
# # print(x*y)
# # print(np.dot(x, y))  
# # print(np.mean(x))
# # print(np.std(x))
# # print(np.sum(x))
# # print(np.min(x))
# # print(np.max(x))
# # print(np.median(x))


# # # reshaping arrays
# # print("Original array:", x)
# # print(x.reshape(3,1))
# # print(y.reshape(1,3)) 
# # print(x.flatten())  # Flattening the array


# # silicing
# print(b[:,1])
# print(b[0,:])
# print(b[0,1])
# print(b[0:1, 0:1])  # Slicing the array to get a sub-array

# # stacking arrays
# c = np.array([[5, 6], [7, 8]])
# print("stack array:\n", np.vstack((b, c)))  # Vertical stacking
# print("horizantal stack array:\n", np.hstack((b, c)))  # Horizontal stacking

# # boardcasting
# b= np.array([[1, 2], [3, 4], [5, 6]])
# print("2d array:\n", b)
# c = np.array([5,6])
# print("1d array:\n", c)
# print("broadcasting:\n", b + c)  # Broadcasting addition


# # # # boolean indexing
# a=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# # print(a>5)
# b=a>5
# print(b)
# print(a[a > 5])

# # random numbers
# a = np.random.rand(2, 3)  
# print(a)

# arr = np.random.randint(1, 10, size=(2, 3))   
# print(arr)




# # 3D array
a=np.array([[[1,2],[3,4]],
            [[5,6],[7,8]]])
b=np.array([
    [
        [[4,5],[6,7]],
        [[8,9],[10,11]]
    ],
    [
        [[12,13],[14,15]],
        [[16,17],[18,19]]
    ]
    ])
# print("3D array:\n", a)
# print("4D array:\n", b)
# print("shape of 3D array:", a.shape ,"4D array:", b.shape)
# print("size of 3D array:", a.size, "4D array:", b.size)
# print("number of dimensions of 3D array:", a.ndim, "4D array:", b.ndim)
# print(a+b)
# print(a*b)
# print(np.dot(a,b))  
# print(np.mean(a))
# print(np.std(a))
# print(np.sum(a))
# print(np.min(a))
# print(np.max(a))
# print(np.median(a))

# print("Original array:", a)
# print(a.reshape(2,4))
# # print(b.reshape(1,3)) 
# print(a.flatten()) 
# print(b.flatten())

# # slicing
print(b[:,1])
print(b[:,:,1,:])
print(b[1,1,:,1])
# print(b[0:1, 0:1])  

# print("stack array:\n", np.vstack((a)))  
# print("horizantal stack array:\n", np.hstack((a)) ) 

print(a[a > 4])
print(b[b > 10])
r = np.random.randint(10, 100, size=(2, 2, 2))
print("Random 3D array:\n", r)
b= np.random.randint(10, 100, size=(2, 2, 2, 2))
print("Random 4D array:\n", b)
c=np.array([1,1])
arr=a+c
print("Broadcasting 3D array:\n", arr)  

