"""class MyClass():
    def myfun1(self):
        pass
    def myfun2(self,name):
        print(name)

mc = MyClass()
mc.myfun1()
mc.myfun2('John')"""


"""class MyClass():
    def myfun1(self):
        pass
    @staticmethod
    def myfun2(self,num):
        print(self,num)

mc = MyClass()
mc.myfun1()
mc.myfun2(100,200) #not a good way to call static method
MyClass().myfun2(100,200) #correct way to use static method
"""

"""a,b = 10,20
class MyClass():
    a,b = 30,50
    def myfun1(self,a,b):
        print(a+b) #local variable
        print(self.a+self.b) #class variable
        print(globals()['a']+globals()['b']) #global variable

mc = MyClass()
mc.myfun1(15,70)
        """


'''class MyClass():
    def __init__(self,a,b,c):  #this is constructor
        self.a = a
        self.b = b
        self.c = c

    def display(self):
        print(self.a,self.b,self.c)


mc = MyClass(11210,"Elon","Musk")
mc.display()'''


"""def l_search(alist,target):
    for i in range(0,len(alist)):
        if alist[i] == target:
            return i
    else:
        return None
def verify(index):
    if index is not None:
        print("The value is found in index:", index)
    else:
        print("Value not found")

num = [2,3221,34,545,16,17,98,89,10]
result = l_search(num, 17)
verify(result)"""




'''def b_search(alist, target):
    start = 0
    end = int(len(alist)-1)

    while start <= end:
        mid = (start + end) //2
        if alist[mid] == target:
            return mid
        elif alist[mid] <= target:
            start= mid + 1
        else:
            end= mid - 1
    return None

def verify(index):
    if index is not None:
        print("The value is found at index:", index)
    else:
        print("Value not found")

num = [1,2,64,121,221,345,564,765,1060,890]
result = b_search(num, 121)
verify(result)'''


'''def recur_b_search(alist, target):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) //2

    if alist[mid] == target:
        return alist[mid]
    else:
        if alist[mid] < target:
            return recur_b_search(alist[mid+1:],target)
        else:
            return recur_b_search(alist[:mid],target)

def verify(index):
    if index is not None:
        print("The value is found at index:", index)
    else:
        print("Value not found")
alist = [1,2,3,4,5,6,7,8,11,13,15,16,17,22,24,23,45]
result = recur_b_search(alist,17)
verify(result)'''




'''def bubble_sory(alist):
    ind = int(len(alist)-1)

    for n in range(ind,0,-1):
        for i in range(n):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

num = [21,2,345,12,543,1,1050,232,10]
bubble_sory(num)
print(num)'''

'''import random
def is_sort(alist):
    ind = int(len(alist)-1)
    for i in range(ind):
        if alist[i] > alist[i +1]:
            return False
    return True

def bogo_sort(alist):
    while not is_sort(alist):
        random.shuffle(alist)
    return alist

num = [34,4311,1,4,6,2,1050]
bogo_sort(num)
print(num)
'''

'''def is_sort(alist):
    slist = []
    for i in range(0,len(alist)):
        index_move = selection_sort(alist)
        slist.append(alist.pop(index_move))
    return slist

def selection_sort(alist):
    min_index = 0
    for i in range(1, len(alist)):
        if alist[i] < alist[min_index]:
            min_index = i
    return min_index

num = [34,4311,1,4,6,2,1050]
okk = is_sort(num)
print(okk)'''

'''def quick_sort(alist):
    if len(alist)<=1:
        return alist

    left_side = []
    right_side= []
    pivot = alist[0]

    for i in alist[1:]:
        if i <= pivot:
            left_side.append(i)
        else:
            right_side.append(i)
    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

num = [34,4311,1,4,6,2,1050]
okk = quick_sort(num)
print(okk)'''
