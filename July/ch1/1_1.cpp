#include <iostream>
#include <string>
using namespace std;

int n,len;
string s;

void reverseString(string &s,int from, int to){
  while(from < to){
    char ch = s[from];
    s[from++] = s[to];
    s[to--] = ch;
  }
}

void leftRorateString(string &s,int n,int len){
  reverseString(s,0,n-1);
  reverseString(s,n,len-1);
  reverseString(s,0,len-1);
  cout<<s<<endl;
}

int main()
{
  cout<<"len,n,s>>>"<<endl;
  while (cin>>len>>n>>s) {
    leftRorateString(s,n,len);
  }
  return 0;
}

/*
*  三步反转string
*
*/
