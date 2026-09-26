import numpy as np 

# 1- how can creat array << varName = np.array([1,2,3])
# -- how can add row np.vstack([prices, []]) , coulmn np.hstack([prices,])

# 2- demnetions

# - row only 
Arr1 = np.array([10,20,60,70])

# -- one table >> row & coulmn
Arr2 = np.array([
    #coulmn
    [10,20,60,70] , #row
    [80,70,60,30], #row
    [177,150,80,40] #row
    ])

# --- many table 
Arr3 = np.array([
    #matrix one
    [
      [10,20,30,np.nan],
      [80,70,60,30]
    ],
    #matrix two 
    [
      ['rehab',10,20,30],
      ['ahmad',60,40,30]
    ]
])

# 3- opretions in np
# - what is the shape index 0 for matrix , 1 for row , 2 for coulmn
print(Arr3.shape)

# -- what is demenations 
print(Arr3.ndim)

# --- how many iteam in array 
print(Arr3.size)

# ---- what the data type
print(Arr3.dtype)
#dont accept if enter first row:4 colmoun and second colmon 3 coulmen must equals that
# if i have number + string so u32 >> all iteam string 
# if have number + none >> object
# if have nmber only >> int or float 
# if have number + no.nan >> flaot


# ----- reshape can help tran array
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#resh1= numbers.reshape(5,3)
# cannot reshape because size of array is 12 not 15 but can reshape to 3,4 or 4,3

# ------Slicing >> array[start:stop:step] , numbers[rows, columns] >> stop not debendcy in index must add 1

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    
])
#print(arr[0:1 ,0:4]) #>>one row one 
#print(arr[0:3 ,0:1]) #>>one colmen  
#print(arr[0:3 , 3:4]) #>> last colmen 
#print (arr[0:2 , 1:3]) 

# ------- Broadcasting >> if have array and wnat add valua each iteam without for 

prices = np.array([100, 200, 300, 400])
#print(prices+50) add all matrix
#print(prices*0.15) multeple all matrix

pric = np.array([
    [100, 200, 300],
    [150, 250, 350]
])
result = pric + np.array([10, 20, 30])
#print (result)

# -------- Statistics >>

scores = np.array([
    80, 90, 75, 60, 95,
    88, 72, 91, 85, 77
])

#print(np.median(scores)) # number of the half of all number
#print(np.std(scores)) # تباعد الارقام بين الرقم الوسط 

# --------- Axis >> axis=1 → نتحرك لليمين // axis=0 → ننزل إلى الأسفل
print(np.sum(scores, axis=0))






