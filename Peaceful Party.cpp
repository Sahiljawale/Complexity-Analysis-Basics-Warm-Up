#include<bits/stdc++.h>
using namespace std;



void solve(){
  int a,b,c;
  cin>>a>>b>>c;
  if(a+c>b){
    cout<<a+c<<endl;
  }
  else{
    cout<<b<<endl;
  }
}

int main(){
  int t;
  cin>>t;
  while(t--){
    solve();
  }
  return 0;
}
