//输入字符串，打印出其全排列

//判断回文串解法一
bool isPalindrom(const char *s,int n){
    if(s == 0 || n < 1){
        return false;
    }
    const char *front,*back;
    while(front < back){
        if(*front != *back){
            return false;
        }
        ++front;
        --back;
    }
    return true;

}
//判断回文串解法一

//跳台阶问题解法一
long long Fibonacci(unsigned int n){
    int result[3] = {0,1,2};
    if(n < 2){
        return result[n];
    }
    return Fibonacci(n-1) + Fibonacci(n-2);
}
//跳台阶问题解法二
int climbStairs(int n){
    int dp[3] = {1,1};
    if(n<2){
        return 1;
        }
    for(int i=2;i<=n;i++){
        dp[2] = dp[0] + dp[1];
        dp[0] = dp[1];
        dp[1] = dp[2];
    }
    return dp[2];
}

//奇偶数排序

