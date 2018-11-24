1.请实现一个函数用来找出字符流中第一个只出现一次的字符。

举例说明:

例如，当从字符流中只读出前两个字符“Go”时，第一个只出现一次的字符是‘g’。当从该字符流中读出前六个字符“google”时，第一个只出现1次的字符是”l”。

解题思路:

字符只能一个接着一个从字符流中读出来。可以定义一个数据容器来保存字符在字符流中的位置。当一个字符第一次从字符流中读出来时，把它在字符流中的位置保存到数据容器里。当这个字符再次从字符流中被读出来时，那么它就不是只出现一次的字符，也就可以被忽略了。这时把它在数据容器里保存的值更新成一个特殊的值（比如负值）。

为了尽可能高校地解决这个问题，需要在O(1)时间内往容器里插入一个字符，以及更新一个字符对应的值。这个容器可以用哈希表来实现。用字符的ASCII码作为哈希表的键值，而把字符对应的位置作为哈希表的值。

解题代码:

public class Test {
    /**
     * 题目：请实现一个函数用来找出字符流中第一个只出现一次的字符。
     */
    private static class CharStatistics {
        // 出现一次的标识
        private int index = 0;
        private int[] occurrence = new int[256];

        public CharStatistics() {
            for (int i = 0; i < occurrence.length; i++) {
                occurrence[i] = -1;
            }
        }

        private void insert(char ch) {
            if (ch > 255) {
                throw new IllegalArgumentException( ch + "must be a ASCII char");
            }

            // 只出现一次
            if (occurrence[ch] == -1) {
                occurrence[ch] = index;
            } else {
                // 出现了两次
                occurrence[ch] = -2;
            }

            index++;
        }

        public char firstAppearingOnce(String data) {
            if (data == null) {
                throw new IllegalArgumentException(data);
            }

            for (int i = 0; i < data.length(); i++) {
                insert(data.charAt(i));
            }
            char ch = '\0';
            // 用于记录最小的索引，对应的就是第一个不重复的数字
            int minIndex = Integer.MAX_VALUE;
            for (int i = 0; i < occurrence.length; i++) {
                if (occurrence[i] >= 0 && occurrence[i] < minIndex) {
                    ch = (char) i;
                    minIndex = occurrence[i];
                }
            }

            return ch;
        }
    }
}




2.输入一个字符串，打印出该字符串中字符的所有排列。例如输入字符串abc。则打印出由字符a、b、c 所能排列出来的所有字符串abc、acb、bac 、bca、cab 和cba 。
解题思路:

把一个字符串看成由两部分组成：第一部分为它的第一个字符，第二部分是后面的所有字符。

我们求整个字符串的排列，可以看成两步：首先求所有可能出现在第一个位置的字符，即把第一个字符和后面所有的字符交换。这个时候我们仍把后面的所有字符分成两部分：后面字符的第一个字符，以及这个字符之后的所有字符。

这其实是很典型的递归思路。

解题代码:

public class Test {
    /**
     * 题目：输入一个字符串，打印出该字符事中字符的所有排列。例如输入字符串abc。
     * 则打印出由字符a、b、c 所能排列出来的所有字符串abc、acb、bac、bca、cab和cba。
     *
     * @param chars 待排序的字符数组
     */
    public static void permutation(char[] chars) {
        // 输入较验
        if (chars == null || chars.length < 1) {
            return;
        }
        // 进行排列操作
        permutation(chars, 0);
    }

    /**
     * 求字符数组的排列
     *
     * @param chars 待排列的字符串
     * @param begin 当前处理的位置
     */
    public static void permutation(char[] chars, int begin) {
        // 如果是最后一个元素了，就输出排列结果
        if (chars.length - 1 == begin) {
            System.out.print(new String(chars) + " ");
        } else {
            char tmp;
            // 对当前还未处理的字符串进行处理，每个字符都可以作为当前处理位置的元素
            for (int i = begin; i < chars.length; i++) {
                // 下面是交换元素的位置
                tmp = chars[begin];
                chars[begin] = chars[i];
                chars[i] = tmp;

                // 处理下一个位置
                permutation(chars, begin + 1);
            }
        }
    }
}


3.题目

输入数字n，按顺序打印出从1到n位最大十进数的数值。比如输入3，则打印出1、2、3一直到最大三位数即999。

解题思路

使用一个n位的数组来存储每一位的元素。例如n位3,则000表示为[0,0,0]。

使用递归的方式，存放每一位元素值。

同上，使用一个n位的数组来存储每一位的元素。然后循环执行加1运算，并在数组中进行模拟进位，直到最高位需要进位，则表示循环结束。

解题代码

public class Test {  
  
    /** 
     * 输入数字n，按顺序打印出从1最大的n位十进制数。比如输入3，则打印出1、2、3 一直到最大的3位数即999。 
     * 
     * @param n 数字的最大位数 
     */  
    public static void printOneToNthDigits(int n) {  
        // 输入的数字不能为小于1  
        if (n < 1) {  
            throw new RuntimeException("The input number must larger than 0");  
        }  
        // 创建一个数组用于打存放值  
        int[] arr = new int[n];  
        printOneToNthDigits(0, arr);  
    }  
  
    /** 
     * 输入数字n，按顺序打印出从1最大的n位十进制数。 
     * 
     * @param n   当前处理的是第个元素，从0开始计数 
     * @param arr 存放结果的数组 
     */  
    public static void printOneToNthDigits(int n, int[] arr) {  
  
        // 说明数组已经装满元素  
        if (n >= arr.length) {  
            // 可以输出数组的值  
            printArray(arr);  
        } else {   
            for (int i = 0; i <= 9; i++) {  
                arr[n] = i;  
                printOneToNthDigits(n + 1, arr);  
            }  
        }  
    }  
  
    /** 
     * 输入数组的元素，从左到右，从第一个非0值到开始输出到最后的元素。 
     * 
     * @param arr 要输出的数组 
     */  
    public static void printArray(int[] arr) {  
        // 找第一个非0的元素  
        int index = 0;  
        while (index < arr.length && arr[index] == 0) {  
            index++;  
        }  
  
        // 从第一个非0值到开始输出到最后的元素。  
        for (int i = index; i < arr.length; i++) {  
            System.out.print(arr[i]);  
        }  
        // 条件成立说明数组中有非零元素，所以需要换行  
        if (index < arr.length) {  
            System.out.println();  
        }  
    }  
  
    /** 
     * 输入数字n，按顺序打印出从1最大的n位十进制数。比如输入3，则打印出1、2、3 一直到最大的3位数即999。 
     * 【第二种方法，比上一种少用内存空间】 
     * 
     * @param n 数字的最大位数 
     */  
    public static void printOneToNthDigits2(int n) {  
        // 输入值必须大于0  
        if (n < 1) {  
            throw new RuntimeException("The input number must larger than 0");  
        }  
  
        // 创建一个长度为n的数组  
        int[] arr = new int[n];  
        // 为数组元素赋初始值  
        for (int i = 0; i < arr.length; i++) {  
            arr[i] = 0;  
        }  
  
        // 求结果，如果最高位没有进位就一直进行处理  
        while (addOne(arr) == 0) {  
            printArray(arr);  
        }  
    }  
  
    /** 
     * 对arr表示的数组的最低位加1 arr中的每个数都不能超过9不能小于0，每个位置模拟一个数位 
     * 
     * @param arr 待加数组 
     * @return 判断最高位是否有进位，如果有进位就返回1，否则返回0 
     */  
    public static int addOne(int[] arr) {  
        // 保存进位值，因为每次最低位加1  
        int carry = 1;  
        // 最低位的位置的后一位  
        int index = arr.length;  
  
        do {  
            // 指向上一个处理位置  
            index--;  
            // 处理位置的值加上进位的值  
            arr[index] += carry;  
            // 求处理位置的进位  
            carry = arr[index] / 10;  
            // 求处理位置的值  
            arr[index] %= 10;  
        } while (carry != 0 && index > 0);  
  
        // 如果index=0说明已经处理了最高位，carry>0说明最高位有进位，返回1  
        if (carry > 0 && index == 0) {  
            return 1;  
        }  
  
        // 无进位返回0  
        return 0;  
    }   
} 