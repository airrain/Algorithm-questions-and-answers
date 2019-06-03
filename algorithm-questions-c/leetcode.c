//字符串前面的若干字符移动到字符串后面解法一
 void fun LeftShiftOne(char *s,int n){
     char t = s[0];
     for(int i = 1;i < n;i++){
         s[i - 1] = s[i];
     }
     s[n -1] = t;
 }
 void fun LeftRotateString(char *s,int n,int m){
     while(m--){
         LeftShiftOne(s,n);
     }
 }
 
 //字符串前面的若干字符移动到字符串后面解法二