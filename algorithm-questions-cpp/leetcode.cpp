#include<iostream>
#include<map>
using name std
//输入字符串，打印出其全排列

//判断回文串解法一
bool isPalindrom(const char *s, int n)
{
    if (s == 0 || n < 1)
    {
        return false;
    }
    const char *front, *back;
    while (front < back)
    {
        if (*front != *back)
        {
            return false;
        }
        ++front;
        --back;
    }
    return true;
}
//判断回文串解法一

//跳台阶问题解法一
long long Fibonacci(unsigned int n)
{
    int result[3] = {0, 1, 2};
    if (n < 2)
    {
        return result[n];
    }
    return Fibonacci(n - 1) + Fibonacci(n - 2);
}
//跳台阶问题解法二
int climbStairs(int n)
{
    int dp[3] = {1, 1};
    if (n < 2)
    {
        return 1;
    }
    for (int i = 2; i <= n; i++)
    {
        dp[2] = dp[0] + dp[1];
        dp[0] = dp[1];
        dp[1] = dp[2];
    }
    return dp[2];
}

//奇偶数排序

//有序数组的查找
int BinarySearch(int arr[], int n, int value)
{
    int left = arr[0];
    int right = arr[n - 1];
    while (left <= right)
    {
        int mid = left + (right - left) << 1;
        if (value < arr[mid])
        {
            right = mid - 1;
        }
        else if (value > arr[mid])
        {
            left = mid + 1;
        }
        else
        {
            return mid;
        }
    }
    return -1;
}

//最大连续子数组和
int MaxSubArray(int *a, int n)
{
    int currentRes = 0;
    int maxRes = a[0];
    for (int j = 0; j < n; j++)
    {
        if (currentRes >= 0)
        {
            currentRes += a[j];
        }
        else
        {
            currentRes = 0;
        }
        if (currentRes > maxRes)
        {
            maxRes = currentRes;
        }
    }
    return maxRes;
}

//荷兰国旗

void helan(int arr[],int n){
    int begin = 0;
    int end = n-1;
    int curr = 0;
    while(begin < end){
        if(arr[curr] == 0){
            swap(arr[curr],arr[begin]);
            curr++;
            begin++;
        }
        else if(arr[curr] == 1){
            curr++;
        }
        else{
            swap(arr[curr],arr[end]);
            end--;
        }
    }

}

//输入n个整数，找出其中最小的k个数。例如输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4

//Partition函数
int Partition(int data[],int length,int start,int end){
    if(data == 0 || length <= 0 || start > end || end > length){
        return 0
    }
    // int index = random(start,end);
}

//如何统计⼀段⽂字中每个单词出现的次数
int main(int,char**){
    map<string,int> dict;
    string s;
    while(cin>>s)
        ++dict[s];
    map<string,int>::iterator it = dict.begin()
    for(;it != dict.end();++it)
        cout<<it->first<<": "<<it->second<<"\n";
}

//�����������Ľڵ�
template <class T>
struct node{
	node(T x):key(x),left(0),right(0),parent(0){}
	~node(){
		delete left;
		delete right;
	}
	node* left;
	node* right;
	node* parent;
	T key;
	
};








 
