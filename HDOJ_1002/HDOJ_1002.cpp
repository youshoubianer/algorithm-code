#include <iostream>
#include<cstring>
#include<string>
using namespace std;

string BigNumSum(string a,string b)
{
    int aLen = a.length();
    int bLen = b.length();
    if(aLen>bLen)
    {
        b = string(aLen-bLen,'0')+b;
    }
    else
    {
        a = string(bLen-aLen,'0')+a;
    }

    int numLen = a.length();
    int ci = 0;
    int di = 0;
    for(int i=numLen-1; i>=0; i--)
    {
        int ai = a[i]-'0';
        int bi = b[i]-'0';
        di = ai + bi + ci;
        ci = di / 10;
        a[i] = (di % 10) +'0';
    }
    return ci>0?"1"+a:a;
}

int main()
{
    int t;
    string a,b;
    cin>>t;
    for(int k=1; k<=t; k++)
    {
        cin>>a>>b;
        string sum = BigNumSum(a,b);
        cout<<"Case "<<k<<":"<<endl;
        cout<<a<<" + "<<b<<" = "<<sum<<endl;
        if(k!=t)
            cout<<endl;
    }
    return 0;
}
