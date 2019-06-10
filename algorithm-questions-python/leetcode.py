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
    while(i < len(arr)):
        suma += arr[i]
        sumb += i
        i += 1
    sumb = sumb + len(arr) + len(arr) + 1
    return sumb - suma 

if __name__ == "__main__":
    arr = [123567]
    print(getNum(arr))
