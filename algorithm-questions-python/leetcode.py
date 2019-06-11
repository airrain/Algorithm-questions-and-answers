#对字符串进行反转
def reverseStr(str):
    arr = list(str)
    n = len(arr)
    i = 0
    j = n-1
    while i < j:
        arr[i] = tmp
        tmp = arr[j]
        arr[j] = tmp
        i+=1
        j-=1
        res = ''.join(arr)
    return res

if __name__ == "__main__":
    str = "abcde"
    print("字符串"+str+"反转以后：")
    print(str.reverseStr(str))

#统计字符串中连续的重复字符个数
def getMaxDupChar(s,startIndex,currMaxNum,maxNum):
    if startIndex == len(s):
        return max(currMaxNum,maxNum)
    if list(s)[startIndex] == list(s)[startIndex+1]:
        return getMaxDupChar(s,startIndex+1,currMaxNum+1,maxNum)
    else:
        return getMaxDupChar(s,startIndex+1,1,max(currMaxNum,maxNum))

if __name__ == "__main__":
    print("连续重复字符个数最大值为"+str(getMaxDupChar("aaacccdd",0,1,1)))


#找出数组中丢失的数
def getNum(arr):
    if arr == None or len(arr) <= 0:
        print("数据不合理")
        return -1
    suma = 0
    sumb = 0
    i = 0
    while i < len(arr):
        suma = suma + arr[i]
        sumb = sumb + i
        i += 1
    sumb = sumb + len(arr) + len(arr) + 1
    return sumb - suma 

if __name__ == "__main__":
    arr = [1,2,3,5,6,7]
    print(getNum(arr))

#计算一个数的n次方
def pow(a,n):
    if n==1:
        return a
    if n==0:
        return 1
    if n>1:
        result = 1.0
        i = 0
        while i < n:
            result *= i
            i += 1
        return result
    else:
        result = 1.0
        while i < n:
            result /= i
            i += 1
        return result

if __name__ == "__main__":
    print(pow(2,3))

#找出绝对值最小的数
def getMin(arr):
    if arr == None or len(arr) == 0:
        return 0
    i = 0
    mins = 2**32
    while i < len(arr):
        if abs(arr[i]) < abs(mins):
            mins = arr[i]
        i += 1
    return mins

if __name__ == "__name__":
    arr = [1,4,-5,6,4,3]
    print(getMin(arr)) 
    
#找出数组中唯一重复的数字
def findSame(arr):
    if arr == None:
        return -1
    i = 0
    lens = len(arr)
    HashTable = dict()
    while i < lens:
        HashTable[i] = 0
        i += 1
    j = 0
    while j < lens:
        if HashTable[arr[i]-1] == 0:
            HashTable[arr[i]-1] = 1
            
        else:
            return arr[j]
        j += 1
    return -1

if __name__ == "__name__":
    arr = [1,2,3,1000]
    print(findSame(arr))

#计算一个数的平方根
def squareRoot(n,e):
    new_one = n
    last_one = 1.0
    while new_one-last_one > e:
        new_one = (new_one+last_one)/2
        last_one = n/new_one
    return new_one
if __name__ == "__main__":
    n = 5
    e = 0.000000001
    print(squareRoot(n,e))
    
#找出数组中出现奇数次的数
def get2Num(arr):
    if arr == None or len(arr) <= 0:
        return 0
    dic = dict()
    i = 0
    while i < len(arr):
        if arr[i] not in dic:
            dic[arr[i]] = 1
        else:
            dic[arr[i]] = 1
            i += 1
    for k,v in dic.items(): 
        if v == 1:
            return k

if __name__ == "__main__":
    arr = [2,4,4,6,6,3]
    print(get2Num(arr))