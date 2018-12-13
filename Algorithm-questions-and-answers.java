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


8.题目：

输入n个整数，找出其中最小的k个数。

例子说明：

例如输入4 、5 、1、6、2、7、3 、8 这8 个数字，则最小的4 个数字是1 、2、3 、4

解题思路：

解法一：O(n)时间算法，只有可以修改输入数组时可用。

可以基于Partition函数来解决这个问题。如果基于数组的第k个数字来调整，使得比第k个数字小的所有数字都位于数组的左边，比第k个数字大的所有数字都位于数组的右边。这样调整之后，位于数组中左边的k个数字就是最小的k 个数字（这k 个数字不一定是排序的〉。

解法二： O（nlogk）的算法，精剧适合处理海量数据。

先创建一个大小为k的数据容器来存储最小的k个数字，接下来我们每次从输入的n个整数中读入一个数．如果容器中已有的数字少于k个，则直接把这次读入的整数放入容器之中：如果容器中己有k 数字了，也就是容器己满，此时我们不能再插入新的数字而只能替换已有的数字。找出这己有的k 个数中的最大值，然后1在这次待插入的整数和最大值进行比较。如果待插入的值比当前己有的最大值小，则用这个数替换当前已有的最大值：如果待插入的值比当前已有的最大值还要大，那么这个数不可能是最小的k个整数之一，于是我们可以抛弃这个整数。

因此当容器满了之后，我们要做3 件事情： 一是在k 个整数中找到最大数： 二是有可能在这个容器中删除最大数： 三是有可能要插入一个新的数字。我们可以使用一个大顶堆在O(logk）时间内实现这三步操作。

解题代码：

public class Test {
    /**
     * 大顶堆
     *
     * @param <T> 参数化类型
     */
    private final static class MaxHeap<T extends Comparable<T>> {
        // 堆中元素存放的集合
        private List<T> items;
        // 用于计数
        private int cursor;

        /**
         * 构造一个椎，始大小是32
         */
        public MaxHeap() {
            this(32);
        }

        /**
         * 造诣一个指定初始大小的堆
         *
         * @param size 初始大小
         */
        public MaxHeap(int size) {
            items = new ArrayList<>(size);
            cursor = -1;
        }

        /**
         * 向上调整堆
         *
         * @param index 被上移元素的起始位置
         */
        public void siftUp(int index) {
            T intent = items.get(index); // 获取开始调整的元素对象

            while (index > 0) { // 如果不是根元素
                int parentIndex = (index - 1) / 2; // 找父元素对象的位置
                T parent = items.get(parentIndex);  // 获取父元素对象
                if (intent.compareTo(parent) > 0) { //上移的条件，子节点比父节点大
                    items.set(index, parent); // 将父节点向下放
                    index = parentIndex; // 记录父节点下放的位置
                } else { // 子节点不比父节点大，说明父子路径已经按从大到小排好顺序了，不需要调整了
                    break;
                }
            }

            // index此时记录是的最后一个被下放的父节点的位置（也可能是自身），所以将最开始的调整的元素值放入index位置即可
            items.set(index, intent);
        }

        /**
         * 向下调整堆
         *
         * @param index 被下移的元素的起始位置
         */
        public void siftDown(int index) {
            T intent = items.get(index);  // 获取开始调整的元素对象
            int leftIndex = 2 * index + 1; // // 获取开始调整的元素对象的左子结点的元素位置

            while (leftIndex < items.size()) { // 如果有左子结点
                T maxChild = items.get(leftIndex); // 取左子结点的元素对象，并且假定其为两个子结点中最大的
                int maxIndex = leftIndex; // 两个子节点中最大节点元素的位置，假定开始时为左子结点的位置

                int rightIndex = leftIndex + 1;  // 获取右子结点的位置
                if (rightIndex < items.size()) {  // 如果有右子结点
                    T rightChild = items.get(rightIndex);  // 获取右子结点的元素对象
                    if (rightChild.compareTo(maxChild) > 0) {  // 找出两个子节点中的最大子结点
                        maxChild = rightChild;
                        maxIndex = rightIndex;
                    }
                }

                // 如果最大子节点比父节点大，则需要向下调整
                if (maxChild.compareTo(intent) > 0) {
                    items.set(index, maxChild); // 将子节点向上移
                    index = maxIndex; // 记录上移节点的位置
                    leftIndex = index * 2 + 1; // 找到上移节点的左子节点的位置
                } else { // 最大子节点不比父节点大，说明父子路径已经按从大到小排好顺序了，不需要调整了
                    break;
                }
            }

            // index此时记录是的最后一个被上移的子节点的位置（也可能是自身），所以将最开始的调整的元素值放入index位置即可
            items.set(index, intent);
        }

        /**
         * 向堆中添加一个元素
         *
         * @param item 等待添加的元素
         */
        public void add(T item) {
            items.add(item); // 将元素添加到最后
            siftUp(items.size() - 1); // 循环上移，以完成重构
        }

        /**
         * 删除堆顶元素
         *
         * @return 堆顶部的元素
         */
        public T deleteTop() {
            if (items.isEmpty()) { // 如果堆已经为空，就报出异常
                throw new RuntimeException("The heap is empty.");
            }

            T maxItem = items.get(0); // 获取堆顶元素
            T lastItem = items.remove(items.size() - 1); // 删除最后一个元素
            if (items.isEmpty()) { // 删除元素后，如果堆为空的情况，说明删除的元素也是堆顶元素
                return lastItem;
            }

            items.set(0, lastItem); // 将删除的元素放入堆顶
            siftDown(0); // 自上向下调整堆
            return maxItem; // 返回堆顶元素
        }

        /**
         * 获取下一个元素
         *
         * @return 下一个元素对象
         */
        public T next() {

            if (cursor >= items.size()) {
                throw new RuntimeException("No more element");
            }
            return items.get(cursor);

        }

        /**
         * 判断堆中是否还有下一个元素
         *
         * @return true堆中还有下一个元素，false堆中无下五元素
         */
        public boolean hasNext() {
            cursor++;
            return cursor < items.size();
        }

        /**
         * 获取堆中的第一个元素
         *
         * @return 堆中的第一个元素
         */
        public T first() {
            if (items.size() == 0) {
                throw new RuntimeException("The heap is empty.");
            }
            return items.get(0);
        }

        /**
         * 判断堆是否为空
         *
         * @return true是，false否
         */
        public boolean isEmpty() {
            return items.isEmpty();
        }

        /**
         * 获取堆的大小
         *
         * @return 堆的大小
         */
        public int size() {
            return items.size();
        }

        /**
         * 清空堆
         */
        public void clear() {
            items.clear();
        }

        @Override
        public String toString() {
            return items.toString();
        }
    }

    /**
     * 题目： 输入n个整数，找出其中最小的k个数。
     * 【第二种解法】
     * @param input  输入数组
     * @param output 输出数组
     */
    public static void getLeastNumbers2(int[] input, int[] output) {
        if (input == null || output == null || output.length <= 0 || input.length < output.length) {
            throw new IllegalArgumentException("Invalid args");
        }

        MaxHeap<Integer> maxHeap = new MaxHeap<>(output.length);
        for (int i : input) {
            if (maxHeap.size() < output.length) {
                maxHeap.add(i);
            } else {
                int max = maxHeap.first();
                if (max > i) {
                    maxHeap.deleteTop();
                    maxHeap.add(i);
                }
            }
        }

        for (int i = 0; maxHeap.hasNext(); i++) {
            output[i] = maxHeap.next();
        }
    }


    /**
     * 题目： 输入n个整数，找出其中最小的k个数。
     * 【第一种解法】
     * @param input  输入数组
     * @param output 输出数组
     */
    public static void getLeastNumbers(int[] input, int[] output) {

        if (input == null || output == null || output.length <= 0 || input.length < output.length) {
            throw new IllegalArgumentException("Invalid args");
        }

        int start = 0;
        int end = input.length - 1;
        int index = partition(input, start, end);
        int target = output.length - 1;

        while (index != target) {
            if (index < target) {
                start = index + 1;
            } else {
                end = index - 1;
            }
            index = partition(input, start, end);
        }

        System.arraycopy(input, 0, output, 0, output.length);
    }

    /**
     * 分区算法
     *
     * @param input 输入数组
     * @param start 开始下标
     * @param end   结束下标
     * @return 分区位置
     */
    private static int partition(int[] input, int start, int end) {
        int tmp = input[start];

        while (start < end) {
            while (start < end && input[end] >= tmp) {
                end--;
            }
            input[start] = input[end];

            while (start < end && input[start] <= tmp) {
                start++;
            }
            input[end] = input[start];
        }

        input[start] = tmp;
        return start;
    }
}

9.题目：

输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

例子说明：

例如输入数组{3， 32, 321}，则扫描输出这3 个数字能排成的最小数字321323。

解题思路：

第一种：直观解法

先求出这个数组中所有数字的全排列，然后把每个排列拼起来，最后求出拼起来的数字的最小值。

第二种：排序解法

找到一个排序规则，数组根据这个规则排序之后能排成一个最小的数字。要确定排序规则，就要比较两个数字，也就是给出两个数字m 和n，我们需要确定一个规则判断m 和n 哪个应该排在前面，而不是仅仅比较这两个数字的值哪个更大。

根据题目的要求，两个数字m 和n能拼接成数字m和m。如果mn < nm，那么我们应该打印出m，也就是m 应该排在n 的前面，我们定义此时m 小于n：反之，如果nm < mn，我们定义n小于m。如果mn=nm,m 等于n。在下文中，符号“<”、“>”及“＝”表示常规意义的数值的大小关系，而文字“大于”、“小于”、“等于”表示我们新定义的大小关系。

接下来考虑怎么去拼接数字，即给出数字m和n，怎么得到数字m和m 并比较它们的大小。直接用数值去计算不难办到，但需要考虑到一个潜在的问题就是m 和n 都在int 能表达的范围内，但把它们拼起来的数字mn 和nm 用int 表示就有可能溢出了，所以这还是一个隐形的大数问题。

一个非常直观的解决大数问题的方法就是把数字转换成字符串。另外，由于把数字m 和n 拼接起来得到mn 和nm，它们的位数肯定是相同的，因此比较它们的大小只需要按照字符串大小的比较规则就可以了。

解题代码：

public class Test {

    /**
     * 自定义的排序比较器，实现算法说明的排序原理
     */
    private static class MComparator implements Comparator<String> {

        @Override
        public int compare(String o1, String o2) {

            if (o1 == null || o2 == null) {
                throw new IllegalArgumentException("Arg should not be null");
            }

            String s1 = o1 + o2;
            String s2 = o2 + o1;
            return s1.compareTo(s2);
        }
    }

    /**
     * 快速排序算法
     *
     * @param array      待排序数组
     * @param start      要排序的起始位置
     * @param end        要排序的结束位置
     * @param comparator 自定义的比较器
     */
    private static void quickSort(String[] array, int start, int end, Comparator<String> comparator) {

        if (start < end) {
            String pivot = array[start];
            int left = start;
            int right = end;
            while (start < end) {
                while (start < end && comparator.compare(array[end], pivot) >= 0) {
                    end--;
                }

                array[start] = array[end];

                while (start < end && comparator.compare(array[start], pivot) <= 0) {
                    start++;
                }
                array[end] = array[start];

            }

            array[start] = pivot;

            quickSort(array, left, start - 1, comparator);
            quickSort(array, start + 1, end, comparator);
        }
    }

    /**
     * 题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
     * 打印能拼接出的所有数字中最小的一个。
     * @param array 输入的数组
     * @return 输出结果
     */
    public static String printMinNumber(String[] array) {

        if (array == null || array.length < 1) {
            throw new IllegalArgumentException("Array must contain value");
        }

        MComparator comparator = new MComparator();
        quickSort(array, 0, array.length - 1, comparator);

        StringBuilder builder = new StringBuilder(256);
        for (String s : array) {
            builder.append(s);
        }

        return builder.toString();
    }
}


10.题目：

统计一个数字：在排序数组中出现的次数。

举例说明

例如输入排序数组｛ 1, 2, 3, 3, 3, 3, 4, 5｝和数字3 ，由于3 在这个数组中出现了4 次，因此输出4 。

解题思路：

利用改进的二分算法。

如何用二分查找算法在数组中找到第一个k，二分查找算法总是先拿数组中间的数字和k作比较。如果中间的数字比k大，那么k只有可能出现在数组的前半段，下一轮我们只在数组的前半段查找就可以了。如果中间的数字比k小，那么k只有可能出现在数组的后半段，下一轮我们只在数组的后半乓查找就可以了。如果中间的数字和k 相等呢？我们先判断这个数字是不是第一个k。如果位于中间数字的前面一个数字不是k,此时中间的数字刚好就是第一个k。如果中间数字的前面一个数字也是k，也就是说第一个k肯定在数组的前半段， 下一轮我们仍然需要在数组的前半段查找。

同样的思路在排序数组中找到最后一个k。如果中间数字比k大，那么k只能出现在数组的前半段。如果中间数字比k小，k就只能出现在数组的后半段。如果中间数字等于k呢？我们需要判断这个k是不是最后一个k，也就是中间数字的下一个数字是不是也等于k。如果下一个数字不是k，则中间数字就是最后一个k了：否则下一轮我们还是要在数组的后半段中去查找。

解题代码：

public class Test {
    /**
     * 找排序数组中k第一次出现的位置
     *
     * @param data
     * @param k
     * @param start
     * @param end
     * @return
     */
    private static int getFirstK(int[] data, int k, int start, int end) {
        if (data == null || data.length < 1 || start > end) {
            return -1;
        }

        int midIdx = start + (end - start) / 2;
        int midData = data[midIdx];

        if (midData == k) {
            if (midIdx > 0 && data[midIdx - 1] != k || midIdx == 0) {
                return midIdx;
            } else {
                end = midIdx - 1;
            }
        } else if (midData > k) {
            end = midIdx - 1;
        } else {
            start = midIdx + 1;
        }

        return getFirstK(data, k, start, end);
    }

    /**
     * 找排序数组中k最后一次出现的位置
     *
     * @param data
     * @param k
     * @param start
     * @param end
     * @return
     */
    private static int getLastK(int[] data, int k, int start, int end) {
        if (data == null || data.length < 1 || start > end) {
            return -1;
        }

        int midIdx = start + (end - start) / 2;
        int midData = data[midIdx];

        if (midData == k) {
            if (midIdx + 1 < data.length && data[midIdx + 1] != k || midIdx == data.length - 1) {
                return midIdx;
            } else {
                start = midIdx + 1;
            }
        } else if (midData < k) {
            start = midIdx + 1;
        } else {
            end = midIdx - 1;
        }

        return getLastK(data, k, start, end);
    }

    /**
     * 题目：统计一个数字：在排序数组中出现的次数
     * @param data
     * @param k
     * @return
     */
    public static int getNumberOfK(int[] data, int k) {
        int number = 0;
        if (data != null && data.length > 0) {
            int first = getFirstK(data, k, 0, data.length - 1);
            int last = getLastK(data, k, 0, data.length - 1);

            if (first > -1 && last > -1) {
                number = last - first + 1;
            }
        }

        return number;
    }
}


11.题目:

0, 1, … , n-1 这n个数字排成一个圈圈，从数字0开始每次从圆圏里删除第m个数字。求出这个圈圈里剩下的最后一个数字。

解题思路:

创建一个总共有n 个结点的环形链表，然后每次在这个链表中删除第m 个结点。

解题代码:

public static int lastRemaining(int n, int m) {
    if (n < 1 || m < 1) {
        return -1;
    }

    List<Integer> list = new LinkedList<>();
    for (int i = 0; i < n; i++) {
        list.add(i);
    }

    // 要删除元素的位置
    int idx = 0;

    while (list.size() > 1) {

        // 只要移动m-1次就可以移动到下一个要删除的元素上
        for (int i = 1; i < m; i++) {
            idx = (idx + 1) % list.size();
        }

        list.remove(idx);
    }

    return list.get(0);
}

12.题目：

在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

解题思路：

首先选取数组中右上角的数字。如果该数字等于要查找的数字，查找过程结束。

如果该数字大于要查找的数字，剔除这个数字所在的列：如果该数字小于要查找的数字，剔除这个数字所在的行。

也就是说如果要查找的数字不在数组的右上角，则每－次都在数组的查找范围中剔除行或者一列，这样每一步都可以缩小查找的范围，直到找到要查找的数字，或者查找范围为空。

解题代码：

public class Test {  
    public static boolean find(int[][] matrix, int number) {  

        // 输入条件判断  
        if (matrix == null || matrix.length < 1 || matrix[0].length < 1) {  
            return false;  
        }  

        int rows = matrix.length; // 数组的行数  
        int cols = matrix[1].length; // 数组行的列数  

        int row = 0; // 起始开始的行号  
        int col = cols - 1; // 起始开始的列号  

        // 要查找的位置确保在数组之内  
        while (row >= 0 && row < rows && col >= 0 && col < cols) {  
            if (matrix[row][col] == number) { // 如果找到了就直接退出  
                return true;  
            } else if (matrix[row][col] > number) { // 如果找到的数比要找的数大，说明要找的数在当前数的左边  
                col--; // 列数减一，代表向左移动  
            } else { // 如果找到的数比要找的数小，说明要找的数在当前数的下边  
                row++; // 行数加一，代表向下移动  
            }  
        }  

        return false;  
    }   
}


13.题目：

输入一个递增排序的数组和一个数字s，在数组中查找两个数，得它们的和正好是s。如果有多对数字的和等于s，输出任意一对即可。

举例说明：

例如输入数组｛1 、2 、4、7 、11 、15 ｝和数字15. 由于4+ 11 = 15 ，因此输出4 和11 。

解题思路：

我们先在数组中选择两个数字，如果它们的和等于输入的s，我们就找到了要找的两个数字。如果和小于s 呢？我们希望两个数字的和再大一点。由于数组已经排好序了，我们可以考虑选择较小的数字后面的数字。因为排在后面的数字要大一些，那么两个数字的和也要大一些， 就有可能等于输入的数字s 了。同样， 当两个数字的和大于输入的数字的时候，我们可以选择较大数字前面的数字，因为排在数组前面的数字要小一些。

解题代码：

/**
 * 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得得它们的和正好是s。
 * 如果有多对数字的和等于s，输出任意一对即可。
 *
 * @param data
 * @param sum
 * @return
 */
public static List<Integer> findNumbersWithSum(int[] data, int sum) {
    List<Integer> result = new ArrayList<>(2);

    if (data == null || data.length < 2) {
        return result;
    }

    int ahead = data.length - 1;
    int behind = 0;
    long curSum; // 统计和，取long是防止结果溢出

    while (behind < ahead) {
        curSum = data[behind] + data[ahead];

        if (curSum == sum) {
            result.add(data[behind]);
            result.add(data[ahead]);
            break;
        } else if (curSum < sum) {
            behind++;
        } else {
            ahead--;
        }
    }

    return result;
}


14.题目：

给定一棵二叉搜索树，请找出其中的第k大的结点。

解题思路：

如果按照中序遍历的顺序遍历一棵二叉搜索树，遍历序列的数值是递增排序的。只需要用中序遍历算法遍历一棵二叉搜索树，就很容易找出它的第k大结点。

解题代码:

public class Test {
    private static class BinaryTreeNode {
        private int val;
        private BinaryTreeNode left;
        private BinaryTreeNode right;

        public BinaryTreeNode() {
        }

        public BinaryTreeNode(int val) {
            this.val = val;
        }

        @Override
        public String toString() {
            return val + "";
        }
    }

    public static BinaryTreeNode kthNode(BinaryTreeNode root, int k) {
        if (root == null || k < 1) {
            return null;
        }

        int[] tmp = {k};
        return kthNodeCore(root, tmp);
    }

    private static BinaryTreeNode kthNodeCore(BinaryTreeNode root, int[] k) {
        BinaryTreeNode result = null;

        // 先成左子树中找
        if (root.left != null) {
          result =  kthNodeCore(root.left, k);
        }

        // 如果在左子树中没有找到
        if (result == null) {
            // 说明当前的根结点是所要找的结点
            if(k[0] == 1) {
                result = root;
            } else {
                // 当前的根结点不是要找的结点，但是已经找过了，所以计数器减一
                k[0]--;
            }
        }

        // 根结点以及根结点的左子树都没有找到，则找其右子树
        if (result == null && root.right != null) {
            result = kthNodeCore(root.right, k);
        }

        return result;
    }
}

15.题目：

请实现一个函数，把字符串中的每个空格替换成"%20"，例如“We are happy.”，则输出“We%20are%20happy.”。

解题思路：

先判断字符串中空格的数量。根据数量判断该字符串有没有足够的空间替换成"%20"。

如果有足够空间，计算出需要的空间。根据最终需要的总空间，维护一个指针在最后。从后到前，遇到非空的就把该值挪到指针指向的位置，然后指针向前一位，遇到“ ”，则指针前移，依次替换为“02%”。

解题代码：

public class Test {  
    /** 
     * 请实现一个函数，把字符串中的每个空格替换成"%20"，例如“We are happy.“，则输出”We%20are%20happy.“。 
     * 
     * @param string     要转换的字符数组 
     * @param usedLength 已经字符数组中已经使用的长度 
     * @return 转换后使用的字符长度，-1表示处理失败 
     */  
    public static int replaceBlank(char[] string, int usedLength) {  
        // 判断输入是否合法  
        if (string == null || string.length < usedLength) {  
            return -1;  
        }  
  
        // 统计字符数组中的空白字符数  
        int whiteCount = 0;  
        for (int i = 0; i < usedLength; i++) {  
            if (string[i] == ' ') {  
                whiteCount++;  
            }  
        }  
  
        // 计算转换后的字符长度是多少  
        int targetLength = whiteCount * 2 + usedLength;  
        int tmp = targetLength; // 保存长度结果用于返回  
        if (targetLength > string.length) { // 如果转换后的长度大于数组的最大长度，直接返回失败  
            return -1;  
        }  
  
        // 如果没有空白字符就不用处理  
        if (whiteCount == 0) {  
            return usedLength;  
        }  
  
        usedLength--; // 从后向前，第一个开始处理的字符  
        targetLength--; // 处理后的字符放置的位置  
  
        // 字符中有空白字符，一直处理到所有的空白字符处理完  
        while (usedLength >= 0 && usedLength < targetLength) {  
            // 如是当前字符是空白字符，进行"%20"替换  
            if (string[usedLength] == ' ') {  
                string[targetLength--] = '0';  
                string[targetLength--] = '2';  
                string[targetLength--] = '%';  
            } else { // 否则移动字符  
                string[targetLength--] = string[usedLength];  
            }  
            usedLength--;  
        }  
  
        return tmp;  
    }  
}  


16.题目

请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如把9表示成二进制1001，有2位1。因此如果输入9，该函数输出2。

解题思路：

①位移＋计数 每次右移一位，不断和1进行与运算，直到位0。

②循环让(n - 1) & n。如果n的二进制表示中有k个1，那么这个方法只需要循环k次即可。**其原理是不断清除n的二进制表示中最右边的1，同时累加计数器，直至n为0。**因为从二进制的角度讲，n相当于在n - 1的最低位加上1。举个例子，8（1000）= 7（0111）+ 1（0001），所以8 & 7 = （1000）&（0111）= 0（0000），清除了8最右边的1（其实就是最高位的1，因为8的二进制中只有一个1）。再比如7（0111）= 6（0110）+ 1（0001），所以7 & 6 = （0111）&（0110）= 6（0110），清除了7的二进制表示中最右边的1（也就是最低位的1）。

解题代码：

public class Test {  
  
    /** 
     * 请实现一个函数， 输入一个整数，输出该数二进制表示中1的个数。 
     * 例如把9表示成二进制是1001 ，有2位是1. 因此如果输入9，该出2。 
     * 
     * @param n 待的数字 
     * @return 数字中二进制表表的1的数目 
     */  
    public static int numberOfOne(int n) {  
        // 记录数字中1的位数  
        int result = 0;  
  
        // JAVA语言规范中，int整形占四个字节，总计32位  
        // 对每一个位置与1进行求与操作，再累加就可以求出当前数字的表示是多少位1  
        for (int i = 0; i < 32; i++) {  
            result += (n & 1);  
            n >>>= 1;  
        }  
  
        // 返回求得的结果  
        return result;  
    }  
  
    /**
     * @param n 待的数字 
     * @return 数字中二进制表表的1的数目 
     */  
    public static int numberOfOne2(int n) {  
        // 记录数字中1的位数  
        int result = 0;  
  
        // 数字的二进制表示中有多少个1就进行多少次操作  
        while (n != 0) {  
            result++;  
            // 从最右边的1开始，每一次操作都使n的最右的一个1变成了0，  
            // 即使是符号位也会进行操作。  
            n = (n - 1) & n;  
        }  
  
        // 返回求得的结果  
        return result;  
    }    
}  


17.题目：

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数appendTail 和deleteHead，分别完成在队列尾部插入结点和在队列头部删除结点的功能。

解题思路：

栈1用于存储元素，栈2用于弹出元素，负负得正。

说的通俗一点，现在把数据1、2、3分别入栈一，然后从栈一中出来（3、2、1），放到栈二中，那么，从栈二中出来的数据（1、2、3）就符合队列的规律了，即负负得正。

解题代码：

public class Test {  
    public static class MList<T> {  
        // 插入栈，只用于插入的数据  
        private Stack<T> stack1 = new Stack<>();  
        // 弹出栈，只用于弹出数据  
        private Stack<T> stack2 = new Stack<>();  
  
        public MList() {  
        }  
          
        // 添加操作，成在队列尾部插入结点  
        public void appendTail(T t) {  
            stack1.add(t);  
        }  
  
        // 删除操作，在队列头部删除结点  
        public T deleteHead() {  
  
            // 先判断弹出栈是否为空，如果为空就将插入栈的所有数据弹出栈，  
            // 并且将弹出的数据压入弹出栈中  
            if (stack2.isEmpty()) {  
                while (!stack1.isEmpty()) {  
                    stack2.add(stack1.pop());  
                }  
            }  
  
            // 如果弹出栈中还没有数据就抛出异常  
            if (stack2.isEmpty()) {  
                throw new RuntimeException("No more element.");  
            }  
  
            // 返回弹出栈的栈顶元素，对应的就是队首元素。  
            return stack2.pop();  
        }  
    }  
}  


18.题目：

我们把只包含因子2、3 和5 的数称作丑数（Ugly Number）。求从小到大的顺序的第1500个丑数。

举例说明：

例如6、8 都是丑数，但14 不是，它包含因子7。习惯上我们把1 当做第一个丑数。

解题思路：

第一种：逐个判断每个数字是不是丑数的解法，直观但不够高效。

第二种：创建数组保存已经找到丑数，用空间换时间的解法。

根据丑数的定义， 丑数应该是另一个丑数乘以2、3 或者5 的结果（1除外）。因此我们可以创建一个数组，里面的数字是排好序的丑数，每一个丑数都是前面的丑数乘以2、3或者5得到的。

这种思路的关键在于怎样确保数组里面的丑数是排好序的。假设数组中已经有若干个丑数排好序后存放在数组中，并且把己有最大的丑数记做M，我们接下来分析如何生成下一个丑数。该丑数肯定是前面某一个丑数乘以2、3 或者5 的结果， 所以我们首先考虑把已有的每个丑数乘以2。在乘以2 的时候能得到若干个小于或等于M 的结果。由于是按照顺序生成的，小于或者等于M 肯定己经在数组中了，我们不需再次考虑：还会得到若干个大于M 的结果，但我们只需要第一个大于M 的结果，因为我们希望丑数是按从小到大的顺序生成的，其他更大的结果以后再说。我们把得到的第一个乘以2 后大于M 的结果记为M2，同样，我们把已有的每一个丑数乘以3 和5，能得到第一个大于M 的结果M3 和M5，那么下一个丑数应该是M2、M3 和M5这3个数的最小者。

前面分析的时候，提到把已有的每个丑数分别都乘以2、3 和5。事实上这不是必须的，因为已有的丑数是按顺序存放在数组中的。对乘以2而言， 肯定存在某一个丑数T2，排在它之前的每一个丑数乘以2 得到的结果都会小于已有最大的丑数，在它之后的每一个丑数乘以2 得到的结果都会太大。我们只需记下这个丑数的位置， 同时每次生成新的丑数的时候，去更新这个T2。对乘以3 和5 而言， 也存在着同样的T3和T5。

解题代码：

public class Test {
    /**
     * 判断一个数是否只有2，3，5因子（丑数）
     *
     * @param num 待判断的数，非负
     * @return true是丑数，false丑数
     */
    private static boolean isUgly(int num) {
        while (num % 2 == 0) {
            num /= 2;
        }

        while (num % 3 == 0) {
            num /= 3;
        }

        while (num % 5 == 0) {
            num /= 5;
        }

        return num == 1;
    }

    /**
     * 找第index个丑数，速度太慢
     *
     * @param index 第index个丑数
     * @return 对应的丑数值
     */
    public static int getUglyNumber(int index) {
        if (index <= 0) {
            return 0;
        }

        int num = 0;
        int uglyFound = 0;
        while (uglyFound < index) {
            num++;
            if (isUgly(num)) {
                ++uglyFound;
            }
        }

        return num;
    }

    /**
     * 找第index个丑数，【第二种方法】
     *
     * @param index 第index个丑数
     * @return 对应的丑数值
     */
    public static int getUglyNumber2(int index) {
        if (index <= 0) {
            return 0;
        }

        int[] pUglyNumbers = new int[index];
        pUglyNumbers[0] = 1;
        int nextUglyIndex = 1;

        int p2 = 0;
        int p3 = 0;
        int p5 = 0;

        while (nextUglyIndex < index) {
            int min = min(pUglyNumbers[p2] * 2, pUglyNumbers[p3] * 3, pUglyNumbers[p5] * 5);
            pUglyNumbers[nextUglyIndex] = min;

            while (pUglyNumbers[p2] * 2 <= pUglyNumbers[nextUglyIndex]) {
                p2++;
            }

            while (pUglyNumbers[p3] * 3 <= pUglyNumbers[nextUglyIndex]) {
                p3++;
            }

            while (pUglyNumbers[p5] * 5 <= pUglyNumbers[nextUglyIndex]) {
                p5++;
            }

            nextUglyIndex++;
        }

        return pUglyNumbers[nextUglyIndex - 1];
    }

    private static int min(int n1, int n2, int n3) {
        int min = n1 < n2 ? n1 : n2;
        return min < n3 ? min : n3;
    }
}


19.题目：

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小数的min 函数。在该栈中，调用min、push 及pop的时间复杂度都是O(1)。

解题思路：

把每次的最小元素（之前的最小元素和新压入战的元素两者的较小值）都保存起来放到另外一个辅助栈里。

如果每次都把最小元素压入辅助栈， 那么就能保证辅助栈的栈顶一直都是最小元素．当最小元素从数据栈内被弹出之后，同时弹出辅助栈的栈顶元素，此时辅助栈的新栈顶元素就是下一个最小值。

解题代码：

public class MinStack {

    private Stack<Integer> stack = new Stack<Integer>();
    private Stack<Integer> minStack = new Stack<Integer>(); //辅助栈：栈顶永远保存stack中当前的最小的元素


    public void push(int data) {
        stack.push(data);  //直接往栈中添加数据

        //在辅助栈中需要做判断
        if (minStack.size() == 0 || data < minStack.peek()) {
            minStack.push(data);
        } else {
            minStack.add(minStack.peek());   //【核心代码】peek方法返回的是栈顶的元素
        }
    }

    public int pop() throws Exception {
        if (stack.size() == 0) {
            throw new Exception("栈中为空");
        }

        int data = stack.pop();
        minStack.pop();  //核心代码
        return data;
    }

    public int min() throws Exception {
        if (minStack.size() == 0) {
            throw new Exception("栈中空了");
        }
        return minStack.peek();
    }
}


20.题目：

输入两个整数序列，第一个序列表示栈的压入顺序，请判断二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。

解题思路：

解决这个问题很直观的想法就是建立一个辅助栈，把输入的第一个序列中的数字依次压入该辅助栈，并按照第二个序列的顺序依次从该栈中弹出数字。

判断一个序列是不是栈的弹出序列的规律：如果下一个弹出的数字刚好是栈顶数字，那么直接弹出。如果下一个弹出的数字不在栈顶，我们把压栈序列中还没有入栈的数字压入辅助栈，直到把下一个需要弹出的数字压入栈顶为止。如果所有的数字都压入栈了仍然没有找到下一个弹出的数字，那么该序列不可能是一个弹出序列。

解题代码：

public class StackTest {


    //方法：data1数组的顺序表示入栈的顺序。现在判断data2的这种出栈顺序是否正确
    public static boolean sequenseIsPop(int[] data1, int[] data2) {
        Stack<Integer> stack = new Stack<Integer>(); //这里需要用到辅助栈

        for (int i = 0, j = 0; i < data1.length; i++) {
            stack.push(data1[i]);

            while (stack.size() > 0 && stack.peek() == data2[j]) {
                stack.pop();
                j++;
            }
        }
        return stack.size() == 0;
    }
}

21.题目：

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回true。否则返回false。假设输入的数组的任意两个数字都互不相同。

解题思路：

在后序遍历得到的序列中， 最后一个数字是树的根结点的值。数组中前面的数字可以分为两部分： 第一部分是左子树结点的值，它们都比根结点的值小： 第二部分是右子树结点的值，它们都比根结点的值大。

解题代码：

public class Test {
    /**
     * 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
     * 如果是则返回true。否则返回false。假设输入的数组的任意两个数字都互不相同。
     *
     * @param sequence 某二叉搜索树的后序遍历的结果
     * @return true：该数组是某二叉搜索树的后序遍历的结果。false：不是
     */
    public static boolean verifySequenceOfBST(int[] sequence) {

        // 输入的数组不能为空，并且有数据
        if (sequence == null || sequence.length <= 0) {
            return false;
        }

        // 有数据，就调用辅助方法
        return verifySequenceOfBST(sequence, 0, sequence.length - 1);
    }

    /**
     * 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
     * @param sequence 某二叉搜索树的后序遍历的结果
     * @param start    处理的开始位置
     * @param end      处理的结束位置
     * @return true：该数组是某二叉搜索树的后序遍历的结果。false：不是
     */
    public static boolean verifySequenceOfBST(int[] sequence, int start, int end) {

        // 如果对应要处理的数据只有一个或者已经没有数据要处理（start>end）就返回true
        if (start >= end) {
            return true;
        }

        // 从左向右找第一个不小于根结点（sequence[end]）的元素的位置
        int index = start;
        while (index < end - 1 && sequence[index] < sequence[end]) {
            index++;
        }

        // 执行到此处[start, index-1]的元素都是小于根结点的（sequence[end]）
        // [start, index-1]可以看作是根结点的左子树

        // right用于记录第一个大于根结点的元素的位置

        int right = index;

        // 接下来要保证[index, end-1]的所有元素都是大于根根点的值
        // 因为[index, end-1]是根结点的右子树
        // 从第一个不小于根结点的元素开始，找第一个不大于根结点的元素
        while (index < end - 1 && sequence[index] > sequence[end]) {
            index++;
        }
        // 如果[index, end-1]中有小于等于根结点的元素，
        // 不符合二叉搜索树的定义，返回false
        if (index != end - 1) {
            return false;
        }

        // 执行到此处说明直到目前为止，还是合法的
        // [start, index-1]为根结点左子树的位置
        // [index, end-1]为根结点右子树的位置
        index = right;
        return verifySequenceOfBST(sequence, start, index - 1) && verifySequenceOfBST(sequence, index, end - 1);
    }
}

22.题目：

请完成一个函数，输入一个二叉树，该函数输出它的镜像。

解题思路：

先前序遍历这棵树的每个结点，如果遍历到的结点有子结点，就交换它的两个子结点。当交换完所有非叶子结点的左右子结点之后，就得到了树的镜像。

解题代码：

public class Test {
    /**
     * 二叉树的树结点
     */
    public static class BinaryTreeNode {
        int value;
        BinaryTreeNode left;
        BinaryTreeNode right;
    }

    /**
     * 请完成一个函数，输入…个二叉树，该函数输出它的镜像
     *
     * @param node 二叉树的根结点
     */
    public static void mirror(BinaryTreeNode node) {
        // 如果当前结点不为空则进行操作
        if (node != null) {
            // 下面是交换结点左右两个子树
            BinaryTreeNode tmp = node.left;
            node.left = node.right;
            node.right = tmp;

            // 对结点的左右两个子树进行处理
            mirror(node.left);
            mirror(node.right);
        }
    }
}

23.题目：

给定单向链表的一个头指针和节点指针，定义一个函数在O(1)时间删除该节点。

解题思路：

由于给定了节点指针，那么要删除该节点。只要把该节点的值替换为下一个节点的值，同时让该节点直接指向下一个节点的下一个节点。相当于顶包代替了下一个节点，该节点自然就不存在。

需要注意的是如果指定节点是头结点，那么直接把头结点定义为下一个节点即可。如果是尾节点，需要循环遍历到该节点，然后让尾节点的上一个节点的指针为空即可。

解题代码：

public class Test {  
    /** 
     * 链表结点 
     */  
    public static class ListNode {  
        int value; // 保存链表的值  
        ListNode next; // 下一个结点  
    }  
  
    /** 
     * 给定单向链表的头指针和一个结点指针，定义一个函数在0(1)时间删除该结点, 
     * 【注意1：这个方法和文本上的不一样，书上的没有返回值，这个因为JAVA引用传递的原因， 
     * 如果删除的结点是头结点，如果不采用返回值的方式，那么头结点永远删除不了】 
     * 【注意2：输入的待删除结点必须是待链表中的结点，否则会引起错误，这个条件由用户进行保证】 
     * 
     * @param head        链表表的头 
     * @param toBeDeleted 待删除的结点 
     * @return 删除后的头结点 
     */  
    public static ListNode deleteNode(ListNode head, ListNode toBeDeleted) {  
  
        // 如果输入参数有空值就返回表头结点  
        if (head == null || toBeDeleted == null) {  
            return head;  
        }  
  
        // 如果删除的是头结点，直接返回头结点的下一个结点  
        if (head == toBeDeleted) {  
            return head.next;  
        }  
  
        // 下面的情况链表至少有两个结点  
  
        // 在多个节点的情况下，如果删除的是最后一个元素  
        if (toBeDeleted.next == null) {  
            // 找待删除元素的前驱  
            ListNode tmp = head;  
            while (tmp.next != toBeDeleted) {  
                tmp = tmp.next;  
            }  
            // 删除待结点  
            tmp.next = null;  
  
        }  
        // 在多个节点的情况下，如果删除的是某个中间结点  
        else {  
            // 将下一个结点的值输入当前待删除的结点  
            toBeDeleted.value = toBeDeleted.next.value;  
            // 待删除的结点的下一个指向原先待删除引号的下下个结点，即将待删除的下一个结点删除  
            toBeDeleted.next = toBeDeleted.next.next;  
        }  
  
        // 返回删除节点后的链表头结点  
        return head;  
    }  
}  

24.题目：

定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的头结点。

解题思路：

①遍历。将指向下一个节点的指针指向上一个节点。

②递归。先让指向下一个节点的指针为空，然后递归调用，最后再将指向下一个节点的指针指向上一个节点。

解题代码：

遍历

    /**
     * 反转单链表
     * @param head
     * @return
     */
    private static Node reverseHead(Node head) {
        if (head == null) {
            return head;
        }

        Node pre = head;
        Node cur = head.nextNode;
        Node next = null;
        while(cur != null){
            next = cur.nextNode;
            cur.nextNode = pre;

            pre = cur;
            cur = next;
        }
        head.nextNode = null;
        head = pre;
        return head;
    }
递归

    /**
     * 递归反转
     * @param head
     * @return
     */
    private static Node reverseByRecur(Node current) {
        if (current == null || current.nextNode == null) return current;  
         Node nextNode = current.nextNode;  
         current.nextNode = null;  
         Node reverseRest = reverseByRecur(nextNode);  
         nextNode.nextNode = current;  
         return reverseRest;  
    }


25.题目：

输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如：前序遍历序列｛ 1, 2, 4, 7, 3, 5, 6, 8｝和中序遍历序列｛4, 7, 2, 1, 5, 3, 8，6}，重建二叉树并输出它的头结点。

解题思路：

由前序遍历的第一个节点可知根节点。根据根节点，可以将中序遍历划分成左右子树。在前序遍历中找出对应的左右子树，其第一个节点便是根节点的左右子节点。按照上述方式递归便可重建二叉树。

解题代码：

public class Test {  
    /** 
     * 二叉树节点类 
     */  
    public static class BinaryTreeNode {  
        int value;  
        BinaryTreeNode left;  
        BinaryTreeNode right;  
    }  
  
    /** 
     * 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二节树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。 
     * 
     * @param preorder 前序遍历 
     * @param inorder  中序遍历 
     * @return 树的根结点 
     */  
    public static BinaryTreeNode construct(int[] preorder, int[] inorder) {  
        // 输入的合法性判断，两个数组都不能为空，并且都有数据，而且数据的数目相同  
        if (preorder == null || inorder == null || preorder.length != inorder.length || inorder.length < 1) {  
            return null;  
        }  
  
        return construct(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1);  
    }  
  
    /** 
     * 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二节树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。 
     * 
     * @param preorder 前序遍历 
     * @param ps       前序遍历的开始位置 
     * @param pe       前序遍历的结束位置 
     * @param inorder  中序遍历 
     * @param is       中序遍历的开始位置 
     * @param ie       中序遍历的结束位置 
     * @return 树的根结点 
     */  
    public static BinaryTreeNode construct(int[] preorder, int ps, int pe, int[] inorder, int is, int ie) {  
  
        // 开始位置大于结束位置说明已经没有需要处理的元素了  
        if (ps > pe) {  
            return null;  
        }  
        // 取前序遍历的第一个数字，就是当前的根结点  
        int value = preorder[ps];  
        int index = is;  
        // 在中序遍历的数组中找根结点的位置  
        while (index <= ie && inorder[index] != value) {  
            index++;  
        }  
  
        // 如果在整个中序遍历的数组中没有找到，说明输入的参数是不合法的，抛出异常  
        if (index > ie) {  
            throw new RuntimeException("Invalid input");  
        }  
  
        // 创建当前的根结点，并且为结点赋值  
        BinaryTreeNode node = new BinaryTreeNode();  
        node.value = value;  
  
        // 递归构建当前根结点的左子树，左子树的元素个数：index-is+1个  
        // 左子树对应的前序遍历的位置在[ps+1, ps+index-is]  
        // 左子树对应的中序遍历的位置在[is, index-1]  
        node.left = construct(preorder, ps + 1, ps + index - is, inorder, is, index - 1);  
        // 递归构建当前根结点的右子树，右子树的元素个数：ie-index个  
        // 右子树对应的前序遍历的位置在[ps+index-is+1, pe]  
        // 右子树对应的中序遍历的位置在[index+1, ie]  
        node.right = construct(preorder, ps + index - is + 1, pe, inorder, index + 1, ie);  
  
        // 返回创建的根结点  
        return node;  
    }    
}  