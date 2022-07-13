'''n = 5
sum = 0
for i in range(0,n+1):
    sum = sum + i

print(sum)

def palindrome(x):
    return x == x[::-1]'''


'''letter = 9009
letter = str(letter)
fun = palindrome(letter)
if fun == True:
    print("Yes")
else:
    print("No")'''


n = 8
if n > 1:
    for i in range(2,n):
        if (n%i) == 0:
            print("not prime")
            break
    else:
        print("prime")

'''import collections


arr = [1,23,2,1,24,23,23,2]

arr = dict(collections.Counter(arr))
print(arr)'''



'''arr = [5,4,9,2,3]
x= sorted(arr)
print(x)

sum= x[-1]+x[-2]
print(sum)'''


'''def l_search(alist,target):
    ind = int(len(alist))
    for i in range(0,ind):
        if alist[i] == target:
            print("Yes Found!!")
            return target
    else:
        print("Not Found")
        return None

alist = [1,32,43,15,20]
tar = 17
l = l_search(alist,tar)
print(l)
'''


'''arr = [2,43,2,3,7,9]
arr.insert(3,14)
x= int(len(arr))
for i in range(0,x):
    print(arr[i])'''
