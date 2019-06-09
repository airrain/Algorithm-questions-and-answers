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
