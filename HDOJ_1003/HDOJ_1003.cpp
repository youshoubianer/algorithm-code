#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int idx = 1;idx<=t;idx++){
        int n;
        cin>>n;
        int sum = 0;
        int maxn = -0x3f3f3f3f;
        int st,en,a;
        int i,j;
        for(i=j=1;j<=n;j++){
            cin>>a;
            sum += a;
            if(sum > maxn){
                maxn = sum;
                st = i;
                en = j;
            }
            if(sum<0){
                sum = 0;
                i=j+1;
            }
        }

        cout<<"Case "<<idx<<":"<<endl;
        cout<<maxn<<" "<<st<<" "<<en<<endl;
        if(idx!=t)
            cout<<endl;
    }
    return 0;
}
