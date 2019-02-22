"""
获得用户输入的整数n，输出 1!+2!+…+n!的值。
如果输入数值为0、负数、非数字或非整数，输出提示信息：输入有误，请输入正整数。
"""
def main():
    a = input()
    sum = 0
    if a.isdigit():
        n = eval(a)
        if n > 0:
            fact = 1
            for i in range(1,n + 1):
                fact *= i
                sum += fact
            print(sum)
        else:
            print("False")
    else:
        print("False")

main()

