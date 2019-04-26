"""
恺撒密码是古罗马凯撒大帝用来对军事情报进行加解密的算法，它采用了替换方法对信息中的每一个英文字符循环替换为字母表序列中该字符后面的第三个字符，即，字母表的对应关系如下：

原文：A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

密文：D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

对于原文字符P，其密文字符C满足如下条件：C = (P+3) mod 26

上述是凯撒密码的加密方法，解密方法反之，即：P = (C-3) mod 26

假设用户可能使用的输入仅包含西文字母，即英文大小写字母a~zA~Z和特殊字符，请编写一个程序，对输入字符串进行凯撒密码加密，直接输出结果，其中特殊字符不进行加密处理。

注意要点：

需要区分英文字母的大小写。

"""
def encryption(str,n):
    cipher = []
    for i in range(len(str)):
        if str[i].islower():
            if ord(str[i]) < 123 - n:
                c = chr(ord(str[i]) + n)
                cipher.append(c)
            else:
                c = chr(ord(str[i]) + n - 26)
                cipher.append(c)
        elif str[i].isupper():
            if ord(str[i]) < 91 - n:
                c = chr(ord(str[i]) + n - 26)
                cipher.append(c)
            else:
                c = chr(ord(str[i]) + n - 26)
                cipher.append(c)
        else:
            c = str[i]
            cipher.append(c)
    cipherstr = ('').join(cipher)
    return cipherstr

paintext = input()
ciphertext = encryption(plainttext,3)
print(ciphertext)

                







