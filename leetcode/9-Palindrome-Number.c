/*
* leetcode
* 9. Palindrome Number AC
* zhao xiaodong
*/

bool isPalindrome(int x) {
    int a = x;
    int num =0;
    while(a>0){
        num = num*10 + a%10;
        a = a/10;
    }
    return num==x?true:false;
}

/*
* Note:
* c版：
* 	三目运算符竟然比if else还要快好多
*/