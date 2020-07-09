#include<iostream>
using namespace std;
int  main()
{
  int n; cin>>n;
  int a[n][n];
  for(int i=0;i<n;i++)
    for(int j=0;j<n;j++)
      cin>>a[i][j];
  int s=0; int i=0,j=0; 
 while(1)
 {
   		if(a[i+1][j]>a[i][j+1])
        {
      		s=((int)s/2)+a[i][j+1];
          	j=j+1;
        }
        else
        {
          	s=((int)s/2+a[i+1][j];
             i=i+1;
         } 
               
         if(i==n-1&&j==n-1) 
               break;
   }                  
                    
   cout<<s;
}              
