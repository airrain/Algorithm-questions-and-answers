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
            i += 0
    for k,v in dic.items(): 
        if v == 1:
            return k

if __name__ == "__main__":
    arr = [2,4,4,6,6,3]
    print(get2Num(arr))

#求集合的所有子集


#按要求去构造新的数组

#三个有序数组中找出公共元素
def findCommon(arr1,arr2,arr3):
    i = 0
    j = 0
    k = 0
    len1 = len(arr1)
    len2 = len(arr2)
    len3 = len(arr3)
    while i < len1 and j < len2 and k < len3:
        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            common = arr1[i]
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[k]:
            i += 1
        elif arr2[k] < arr3[k]:
            j += 1
        else:
            k += 1
        return common

if __name__ == "__main__":
    arr1 = [2,3,5,7,11]
    arr2 = [3,5,7,11,23]
    arr3 = [5,7,11,13,15]
    print(findCommon(arr1,arr2,arr3))


#直接交换法对字符串进行反转

#实现两个正整数的除法
def divide(m,n):
    res = 0
    remain = m
    while m >= n:
        m = m - n
        res += 1
    remain  = m
    print(res)

if __name__ == "__main__":
    divide(4,2)

#不用循环输出100个数
def prints(n):
    print(str(n))
    if n > 0:
        prints(n-1)

if __name__ == "__main__":
    prints(100)
      

#找出和相等的数对


#如何拿到最多的金币
import random
def getMaxNum(n):
    if n < 0:
        return 0
    a = [None] * n
    i = 0
    while i < n:
        a[i] = random.uniform(1,n)
        i += 1
    i = 0
    max4 = 0
    while i < 4:
        if a[i] > max4:
            max4 = a[i]
        i += 1
    i = 4
    while i < n-1:
        if a[i] > max4:
            return True
        i += 1
    return False

if __name__ == "__main__":
    test_num = 1000 + 0.0
    i = 0
    success = 0
    while i < test_num:
        if getMaxNum(10):
            success += 1
        i += 1
    print(success/test_num)

#正整数n所有可能的整数组合

#用一个随机函数得到另一个随机函数
import random
def func1():
    return int(round.random(random()))
def func2():
    return 0

#循环移动数组k位
def righrShift(arr,k):
    lens = len(arr)   
    if arr == None:
        return 0
    while k != 0:
        i = lens - 1
        tmp = arr[lens-1]
        while i > 0:
            arr[i] = arr[i-1]
            i -= 1
        arr[0] = tmp
        k -= 1

if __name__ == "__main__":
    arr = [1,3,5,7,9]
    lens = len(arr)
    i = 0
    k = 3
    righrShift(arr,k)
    while i < lens:
        print(arr)
        i += 1

#求解二进制数中1的个数
def countOne(n):
    count = 0
    while n > 0:
        if (n&1) == 1:
            count += 1
        n >>= 1
    return count

if __name__ == "__main__":
    print(countOne(7))


#求解1024！末尾0的个数
def zeroCount(n):


#比较两个数的大小
def maxNum(a,b):
    return (a+b+abs(a-b))/2

if __name__ == "__main__":
    print(maxNum(3,5))

'''给一个int型数组，要求找出其中两个和为特定值的数的坐标'''


'''将一个int型的数字转化为罗马数字'''
class Solution(object):
    def intToRoaman(self,num):
        result = ''
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        strings = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = ''
        for i in range(len(num)):
            while num >= nums[i]:
                num -= nums[i]
                result += strings[i]
        return result
    
    if __name__ == "__main__":
        print(Solution().intToRoman(100))

'''翻转一个intger类型的数字'''
class Solution(object):
    def reverse(self,x):
        flag = 0
        if x > 0:
            flag = 1
        elif x < 0:
            flag = -1
        x *= flag
        result = 0
        while x:
            result = result * 10 + x / 10
            x /= 10
        result *= flag
        return result

    if __name__ == "__main__":
        print(Solution().reverse(123))

'''找出一个列表中所有和为零的三元组。要求求出的三元组中没有重复'''



'''将一个链表中的倒数第n个元素从链表中去除'''
class ListNode(object):
    def __init__(self,x):
        self.next = None
        self.val = x
    def myPrint(self):
        print(self.val)
        if self.next:
            self.next.myPrint()
class Solution(object):
    def removeNThnumber(self,head,n):
        if not head:
            return head
        permi = ListNode(-1)
        permi.next = head
        curr = permi
        prev = permi
        while prev and n >= 0:
            prev = prev.next
            n -= 1
        while prev:
            prev = prev.next
            curr = curr.next
        curr.next = curr.next.next
        return permi.next

if __name__ == "__main__":
    n5 = ListNode(5) 
    n4 = ListNode(4)
    n3 = ListNode(3)
    n2 = ListNode(2)
    n1 = ListNode(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    result = Solution().removeNThnumber(n1,2)
    result.myPrint()

'''删除一个数组中某一特定数值的元素，返回删除后的数组长度'''
class Solution(object):
    def removeElement(self,nums,val):
        left = 0
        right = len(nums) - 1
        while left <= right:
            while left <= right and nums[left] != val:
                left += 1
            while left <= right and nums[right] == val:
                right -= 1
            if left < right:
                nums[left] = nums[right]
                left += 1
                right -= 1
        return right + 1
    
if __name__ == "__main__":
    Solution().removeElement([1,2,3,4,3,1]

'''判断给出的数组是否否存在一种跳法跳到最后'''
class Solution(object):
    def canJum(self,nums):
        length = len(nums)
        index = 0
        longest = nums[0]
        if not nums:
            return False
        while index <= longest:
            if longest >= length - 1:
                return True
            longest = max(longest,index + nums[index])
            index += 1
        return False
    
if __name__ == "__main__":
    Solution().canJum([1,3,2,4,2])

'''把一个数字用几个几的形式表示出来'''



'''求x的n次幂'''
class Solution(object):
    def myPow(self,x,n):
        result = 1
        flag = 1 if x >= 0 else -1
        n = abs(n)
        while n > 0:
            if n & 1 == 1:
                result *= x
            n >>= 1
            x *= x
        if flag < 0:
            result = 1/result
        return result
if __name__ == "__main__":
    print(Solution().myPow(2,3))


        


