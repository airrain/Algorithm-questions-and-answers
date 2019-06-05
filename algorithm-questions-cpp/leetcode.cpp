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
