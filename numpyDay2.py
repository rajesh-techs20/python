#INDEXING AND SLICING

arr=np.array([10,20,30,40,50])
print(arr)
#access individual elements
print(arr[0])

#slicing
print(arr[1:4])
print(arr[3:]) #last two elements

#OUTPUT
[10 20 30 40 50]
10
[20 30 40]
[40 50]


#TASK1
c=np.array([5,10,15,20,25,30])
print(c[0]) #first element
print(c[-1]) #last element
print(c[1:5]) #index 1 to 4
print(c[:4]) #first four elements
print(c[3:])  #last 3 elements

#OUTPUT
5
30
[10 15 20 25]
[ 5 10 15 20]
[15 20 25 30]
