//字符串前面的若干字符移动到字符串后面解法一
 void LeftShiftOne(char *s,int n){
     char t = s[0];
     for(int i = 1;i < n;i++){
         s[i - 1] = s[i];
     }
     s[n -1] = t;
 }
 void LeftRotateString(char *s,int n,int m){
     while(m--){
         LeftShiftOne(s,n);
     }
 }
 
 //字符串前面的若干字符移动到字符串后面解法二
 void ReverseString(char *s,int from,int to){
     char t = from;
     s[from++] = s[to];
     s[to--] = t;
 }
 void LeftRotateString(char *s,int n,int m){
     m %= n;
     ReverseString(s,0,m-1);
     ReverseString(s,m,n-1);
     ReverseString(s,0,n-1);
 }

 //判断短字符串包含在长字符串中解法一
 