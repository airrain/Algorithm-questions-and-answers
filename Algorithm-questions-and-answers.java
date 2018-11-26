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


4.题目：

输入一个整型数组，数组里有正数也有负数。数组中一个或连续的多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O(n)。

例子说明：

例如输入的数组为{1, -2, 3, 10, -4, 7, 2, -5}，和最大的子数组为｛3, 10, -4, 7, 2}。因此输出为该子数组的和18 。

解题思路：

解法一：举例分析数组的规律。

我们试着从头到尾逐个累加示例数组中的每个数字。初始化和为0。第一步加上第一个数字1， 此时和为1。接下来第二步加上数字-2，和就变成了-1。第三步刷上数字3。我们注意到由于此前累计的和是－1 ，小于0，那如果用-1 加上3 ，得到的和是2 ， 比3 本身还小。也就是说从第一个数字开始的子数组的和会小于从第三个数字开始的子数组的和。因此我们不用考虑从第一个数字开始的子数组，之前累计的和也被抛弃。

我们从第三个数字重新开始累加，此时得到的和是3 。接下来第四步加10，得到和为13 。第五步加上-4， 和为9。我们发现由于-4 是一个负数，因此累加-4 之后得到的和比原来的和还要小。因此我们要把之前得到的和13 保存下来，它有可能是最大的子数组的和。第六步加上数字7，9 加7 的结果是16，此时和比之前最大的和13 还要大， 把最大的子数组的和由13更新为16。第七步加上2，累加得到的和为18，同时我们也要更新最大子数组的和。第八步加上最后一个数字-5，由于得到的和为13 ，小于此前最大的和18，因此最终最大的子数组的和为18 ，对应的子数组是｛3, 10, -4, 7, 2｝。

解法二： 应用动态归划法。

可以用动态规划的思想来分析这个问题。如果用函数f(i)表示以第i个数字结尾的子数组的最大和，那么我们需要求出max[f(i)]，其中0 <= i < n。我们可用如下边归公式求f(i):



这个公式的意义：当以第i-1 个数字结尾的子数组中所有数字的和小于0时，如果把这个负数与第i个数累加，得到的结果比第i个数字本身还要小，所以这种情况下以第i个数字结尾的子数组就是第i个数字本身。如果以第i-1 个数字结尾的子数组中所有数字的和大于0 ,与第i 个数字累加就得到以第i个数字结尾的子数组中所有数字的和。

解题代码：

public class Test {
    /**
     * 输入一个整型数组，数组里有正数也有负数。数组中一个或连
     * 续的多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O(n)。
     *
     * @param arr 输入数组
     * @return 最大的连续子数组和
     */
    public static int findGreatestSumOfSubArray(int[] arr) {
        // 参数校验
        if (arr == null || arr.length < 1) {
            throw new IllegalArgumentException("Array must contain an element");
        }

        // 记录最大的子数组和，开始时是最小的整数
        int max = Integer.MIN_VALUE;
        // 当前的和
        int curMax = 0;
        // 数组遍历
        for (int i : arr) {
            // 如果当前和小于等于0，就重新设置当前和
            if (curMax <= 0) {
                curMax = i;
            }
            // 如果当前和大于0，累加当前和
            else {
                curMax += i;
            }

            // 更新记录到的最在的子数组和
            if (max < curMax) {
                max = curMax;
            }
        }


        return max;
    }
}

5.题目：

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

解题思路：

解法一：基于Partition 函数的O(n)算法

数组中有一个数字出现的次数超过了数组长度的一半。如果把这个数组排序，那么排序之后位于数组中间的数字一定就是那个出现次数超过数组长度一半的数字。也就是说，这个数字就是统计学上的中位数，即长度为n 的数组中第n/2 大的数字。

这种算法是受快速排序算法的启发。在随机快速排序算法中，我们先在数组中随机选择一个数字，然后调整数组中数字的顺序， 使得比选中的数字小数字都排在它的左边，比选中的数字大的数字都排在它的右边。如果这个选中的数字的下标刚好是n/2，那么这个数字就是数组的中位数。如果它的下标大于n/2 ，那么中位数应该位于它的左边，我们可以接着在它的左边部分的数组中查找。如果它的下标小于n/2，那么中位数应该位于它的右边，我们可以接着在它的右边部分的数组中查找。这是一个典型的递归过程。

解法二：根据数组组特点找出O(n)的算法

数组中有一个数字出现的次数超过数组长度的一半，也就是说它出现的次数比其他所有数字出现次数的和还要多。因此我们可以考虑在遍历数组的时候保存两个值： 一个是数组中的一个数字， 一个是次数。当我们遍历到下一个数字的时候，如果下一个数字和我们之前保存的数字相同，则次数加1，如果下一个数字和我们之前保存的数字不同，则次数减1 。如果次数为零，我们需要保存下一个数字，并把次数设为1 。由于我们要找的数字出现的次数比其他所有数字出现的次数之和还要多，那么要找的数字肯定是最后一次把次数设为1 时对应的数字。

本题采用第二种实现方式

解题代码：

public class Test {

    /**
     * 题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字
     *
     * @param numbers 输入数组
     * @return 找到的数字
     */
    public static int moreThanHalfNum(int[] numbers) {

        // 输入校验
        if (numbers == null || numbers.length < 1) {
            throw new IllegalArgumentException("array length must large than 0");
        }

        // 用于记录出现次数大于数组一半的数
        int result = numbers[0];
        // 于当前记录的数不同的数的个数
        int count = 1;
        // 从第二个数开始向后找
        for (int i = 1; i < numbers.length; i++) {
            // 如果记数为0
            if (count == 0) {
                // 重新记录一个数，假设它是出现次数大于数组一半的
                result = numbers[i];
                // 记录统计值
                count = 1;
            }
            // 如果记录的值与统计值相等，记数值增加
            else if (result == numbers[i]) {
                count++;
            }
            // 如果不相同就减少，相互抵消
            else {
                count--;
            }
        }

        // 最后的result可能是出现次数大于数组一半长度的值
        // 统计result的出现次数
        count = 0;
        for (int number : numbers) {
            if (result == number) {
                count++;
            }
        }

        // 如果出现次数大于数组的一半就返回对应的值
        if (count > numbers.length / 2) {
            return result;
        }
        // 否则输入异常
        else {
            throw new IllegalArgumentException("invalid input");
        }
    }
}


6.题目：

把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s 的所有可能的值出现的概率。

解题思路：

解法一：基于通归求解，时间效率不够高。

先把n个骰子分为两堆：第一堆只有一个，另一个有n- 1 个。单独的那一个有可能出现从1 到6 的点数。我们需要计算从1 到6 的每一种点数和剩下的n-1 个骰子来计算点数和。接下来把剩下的n-1个骰子还是分成两堆，第一堆只有一个， 第二堆有n-2 个。我们把上一轮那个单独骰子的点数和这一轮单独骰子的点数相加， 再和剩下的n-2 个骰子来计算点数和。分析到这里，我们不难发现这是一种递归的思路，递归结束的条件就是最后只剩下一个骰子。

我们可以定义一个长度为6n-n+1 的数组， 和为s 的点数出现的次数保存到数组第s-n个元素里。

解法二：基于循环求解，时间性能好

我们可以考虑用二维数组来存储骰子点数的每一个总数出现的次数。在一次循环中， 第一个数组中的第n 个数字表示骰子和为n 出现的次数。在下一循环中，我们加上一个新的骰子，此时和为n 的骰子出现的次数应该等于上一次循环中骰子点数和为n-1 、n-2 、n-3 、n-4, n-5 与n-6 的次数的总和，所以我们把另一个数组的第n个数字设为前一个数组对应的第n-1 、n-2 、n-3 、n-4、n-5与n-6之和。

解题代码：

public class Test {
    /**
     * 基于通归求解
     *
     * @param number 色子个数
     * @param max    色子的最大值
     */
    public static void printProbability(int number, int max) {
        if (number < 1 || max < 1) {
            return;
        }

        int maxSum = number * max;
        int[] probabilities = new int[maxSum - number + 1];
        probability(number, probabilities, max);

        double total = 1;
        for (int i = 0; i < number; i++) {
            total *= max;
        }

        for (int i = number; i <= maxSum; i++) {
            double ratio = probabilities[i - number] / total;
            System.out.printf("%-8.4f", ratio);
        }

        System.out.println();

    }

    /**
     * @param number        色子个数
     * @param probabilities 不同色子数出现次数的计数数组
     * @param max           色子的最大值
     */
    private static void probability(int number, int[] probabilities, int max) {
        for (int i = 1; i <= max; i++) {
            probability(number, number, i, probabilities, max);
        }
    }

    /**
     * @param original      总的色子数
     * @param current       剩余要处理的色子数
     * @param sum           已经前面的色子数和
     * @param probabilities 不同色子数出现次数的计数数组
     * @param max           色子的最大值
     */
    private static void probability(int original, int current, int sum, int[] probabilities, int max) {
        if (current == 1) {
            probabilities[sum - original]++;
        } else {
            for (int i = 1; i <= max; i++) {
                probability(original, current - 1, i + sum, probabilities, max);
            }
        }
    }

    /**
     * 基于循环求解
     * @param number 色子个数
     * @param max    色子的最大值
     */
    public static void printProbability2(int number, int max) {
        if (number < 1 || max < 1) {
            return;
        }

        int[][] probabilities = new int[2][max * number + 1];
        // 数据初始化
        for (int i = 0; i < max * number + 1; i++) {
            probabilities[0][i] = 0;
            probabilities[1][i] = 0;
        }

        // 标记当前要使用的是第0个数组还是第1个数组
        int flag = 0;

        // 抛出一个骰子时出现的各种情况
        for (int i = 1; i <= max; i++) {
            probabilities[flag][i] = 1;
        }

        // 抛出其它骰子
        for (int k = 2; k <= number; k++) {
            // 如果抛出了k个骰子，那么和为[0, k-1]的出现次数为0
            for (int i = 0; i < k; i++) {
                probabilities[1 - flag][i] = 0;
            }

            // 抛出k个骰子，所有和的可能
            for (int i = k; i <= max * k; i++) {
                probabilities[1 - flag][i] = 0;

                // 每个骰子的出现的所有可能的点数
                for (int j = 1; j <= i && j <= max; j++) {
                    // 统计出和为i的点数出现的次数
                    probabilities[1 - flag][i] += probabilities[flag][i - j];
                }
            }

            flag = 1 - flag;
        }


        double total = 1;
        for (int i = 0; i < number; i++) {
            total *= max;
        }

        int maxSum = number * max;
        for (int i = number; i <= maxSum; i++) {
            double ratio = probabilities[flag][i] / total;
            System.out.printf("%-8.4f", ratio);
        }

        System.out.println();
    }
}

7.题目：

一个整型数组里除了两个数字之外，其他的数字都出现了两次，请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

举例说明：

例如输入数组｛2, 4, 3, 6, 3, 2, 5 }，因为只有4 、6 这两个数字只出现一次，其他数字都出现了两次，所以输出4和6 。

解题思路：

这两个题目都在强调一个（或两个）数字只出现一次，其他的出现两次。这有什么意义呢？我们想到异或运算的一个性质：任何一个数字异或它自己都等于0。也就是说， 如果我们从头到尾依次异或数组中的每一个数字，那么最终的结果刚好是那个只出现一次的数字，因为那些成对出现两次的数字全部在异或中抵消了。

想明白怎么解决这个简单问题之后，我们再回到原始的问题，看看能不能运用相同的思路。我们试着把原数组分成两个子数组，使得每个子数组包含一个只出现一次的数字，而其他数字都成对出现两次。如果能够这样拆分成两个数组， 我们就可以按照前面的办法分别找出两个只出现一次的数字了。

我们还是从头到尾依次异或数组中的每一个数字，那么最终得到的结果就是两个只出现一次的数字的异或结果。因为其他数字都出现了两次，在异或中全部抵消了。由于这两个数字肯定不一样，那么异或的结果肯定不为0，也就是说在这个结果数字的二进制表示中至少就有一位为1 。我们在结果数字中找到第一个为1 的位的位置，记为第n 位。现在我们以第n位是不是１为标准把原数组中的数字分成两个子数组，第一个子数组中每个数字的第n 位都是1 ， 而第二个子数组中每个数字的第n 位都是0。由于我们分组的标准是数字中的某一位是1 还是0 ， 那么出现了两次的数字肯定被分配到同一个子数组。因为两个相同的数字的任意一位都是相同的，我们不可能把两个相同的数字分配到两个子数组中去，于是我们已经把原数组分成了两个子数组，每个子数组都包含一个只出现一次的数字，而其他数字都出现了两次。我们已经知道如何在数组中找出唯一一个只出现一次数字， 因此到此为止所有的问题都已经解决了。

解题代码:

public class Test {
    public static int[] findNumbersAppearanceOnce(int[] data) {
        int[] result = {0, 0};

        if (data == null || data.length < 2) {
            return result;
        }

        int xor = 0;
        for (int i : data) {
            xor ^= i;
        }

        int indexOf1 = findFirstBit1(xor);

        for (int i : data) {
            if (isBit1(i, indexOf1)) {
                result[0] ^= i;
            } else {
                result[1] ^= i;
            }
        }

        return result;
    }

    private static int findFirstBit1(int num) {
        int index = 0;
        while ((num & 1) == 0 && index < 32) {
            num >>>= 1;
            index++;
        }

        return index;
    }

    private static boolean isBit1(int num, int indexBit) {
        num >>>= indexBit;
        return (num & 1) == 1;
    }
}