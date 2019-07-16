#对字符串进行反转
def reverseStr(str):
    arr = list(str)
    n = len(arr)
    i = 0
    j = n-1
    while i < j:
        tmp = arr[i]
        arr[i] = arr[j]
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
    return None

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
    Solution().removeElement([1,2,3,4,3,1])

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

'''在一个集合（没有重复数字）中找到和为特定值的所有组合'''

'''实现两个int型数字的除法，不可以使用乘法、除法和模操作'''

'''找出一组字符串中最长的公共前缀'''
class Solution(object):
    def longestBefore(self,strs):
        if not strs:
            return ''
        longest = strs[0]
        for i in range(len(strs[0])):
            for str in strs:
                if len(strs[i]) < i or str[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

if __name__ == "__main__":
    Solution().longestBefore(['qwer'],['qwse'],['qwdr'])

'''将一个数组中的数字右旋k位，即所有的数字向后移k位，末尾的数字移到开头'''
class Solution(object):
    def rotate(self,nums,k):
            def reverse(nums,start,end):
                while start < end:
                    nums[start],nums[end] = nums[end],nums[start]
                    start += 1
                    end -= 1
            n = len(nums)
            k %= n
            reverse(nums,0,n - k - 1)
            reverse(nums,k - 1,n - 1)
            reverse(nums,0,n - 1)
            
if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    Solution().rotate(nums,5)

'''找出一个无序数组中缺少的最小的正整数'''
class Solution(object):
    def firstMissingPositive(self,nums):
        if not nums:
            return 1
        length = len(nums)
        i = 0
        while i < length:
            current = nums[i]
            if current < 0 or current > length or nums[current - 1] == current:
                i += 1
            else:
                nums[current - 1],nums[i] = nums[i],nums[current - 1]
        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1

if __name__ == "__main__":
    Solution().firstMissingPositive([1,2,4,3,5])

'''给一个由包含一串数字的列表组成的非负整数加上一'''
class Solution(object):
    def plusOne(self,digits):
        for i in range(len(digits - 1),-1,-1):
            carry = 1
            digits[i] += carry
            if digits[i] < 10:
                carry = 0
                break
            else:
                digits -= 10
        if carry == 1:
                digits.insert(0,1)
        return digits
if __name__ == "__main__":
    Solution().plusOne([1,3,5,6,8,9])

'''数组中的每个值表示在当前位置最多能向前面跳几步，判断至少跳几步能够跳到最后'''
class Solution(object):
    def jump(self,nums):
        return None

'''数组中的每个值表示在当前位置最多能向前面跳几步，判断给出的数组是否否存在一种跳法跳到最后。'''
class Solution(object):
    def jump(self,nums):
        if not nums:
            return False
        length = len(nums)
        longest = nums[0]
        index = 0
        while index <= length:
            if longest >= length - 1:
                return True
            longest = max(longest,index + nums[index])
            index += 1
        return False

if __name__ == "__main__":
    Solution().jump([1,3,4,2])

'''对两个二进制的字符串求和'''
class Solution(object):
    def searchRange(self,nums,target):
        length = len(nums)
        result = []
        start = 0
        end = length
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target and (start == 0 or nums[mid - 1] != target):
                result.append(mid)
                break
            if nums[mid] < target:
                start = mid + 1
            else:
                end = length
        if not result:
            return [-1,-1]
        end = length
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target and (end == length or nums[mid + 1] != target):
                result.append(mid)
                break
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = length
        return result

if __name__ == "__main__":
    Solution().searchRange([1,3,4,2,4,4],4)

'''计算一个凹凸不平的模型中可以存放多少的雨水'''


'''在一个集合（没有重复数字）中找到和为特定值的所有组合'''
class Solution(object):
    def combination(self,target,nums):
        if not nums:
            return []
        result = []
        nums.sort()
        self.combination(target,nums,[],result)
        return result
    
    def combination(self,target,nums,current,result):
        s = sum(current) if current else 0
        if s > target:
            return 
        elif s == target:
            result.append(current)
            return
        else:
            for i,v in enumerate(nums):
                self.combination(target,nums[i:],current + v,result)

if __name__ == "__main__":
    Solution().combination(8,[3,2,5,3,2,3])

'''现给定二进制码的位数，要求打印出格雷码序列'''
class Solution(object):
    def greyCode(self,num):
        result = [(i >> 2) ^ i for i in range(pow(2,num))]
        return result
if __name__ == "__main__":
    Solution().greyCode(3)

'''现在有如下的字母与数字的对应关系：1-A, 2-B, ...26-Z。给定一个由数字组成的字符串，判断按照上面的映射可以转换成多少种不同的字符串'''


'''机器人从起点到终点有多少条不同的路径，只能向右或者向下走'''
import math
class Solution(object):
    def findRoad(self,m,n):
        m -= 1
        n -= 1
        return math.factorial(m + n)/math.factorial(m)/math.factorial(n)
if __name__ == "__main__":
    Solution().findRoad(4,6)

'''更常见的一种做法就是动态规划，要到达一个格子只有从它上面或者左边的格子走过来，递推关系式：dp[i][j]=dp[i-1][j]+dp[i][j-1]'''
class Solution(object):
    def uniquePaths(self,m,n):
        dp = [[1 for __ in range(1,n)]for __ in range(1,m)]
        for i in range(1,n):
            for j in range(1,m):
                dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
        return dp[j - 1][i - 1]
if __name__ == "__main__":
    Solution().uniquePaths(3,4)

'''找出一个由纯数字组成的序列能够构成的不同的IP地址。'''

'''求一个数的平方根。'''
class Solution(object):
    def mySqrit(self,x):
        result = 1
        while abs(result * result - x) > 0.1:
            result = (result + x/result)/2
        return result
if __name__ == "__main__":
    Solution().mySqrit(3) 

'''给定一个由不同数字组成的集合，罗列出该集合的所有子集'''
class Solution(object):
    def findSets(self,nums):
        result = [[]]
        for num in sorted(nums):
            result += [item + [num] for item in result]
        return result
if __name__ == "__main__":
    Solution().findSets([2,4,3,3]) 

'''化简Unix系统下一个文件的绝对路径'''

'''罗列出一个包含重复数字的集合的所有的子集'''

'''查找最小的可用id'''
def findMinId(self,nums):
    i = 0
    while True:
        if i not in nums:
            return i
        i = i + 1

'''输入三个字符串s1、s2和s3，判断第三个字符串s3是否由前两个字符串s1和s2交替而成且不改变s1和s2中各个字符原有的相对顺序'''
