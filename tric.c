#include<stdio.h>
#include<math.h>
int main()
     {
     int n,i,k,l,stat,count=0;
     float s;
     printf("\nEnter the value of 'n': ");
     scanf("%d",&n);
     i= sqrt(n);
     for(l=i;l>0;l--)
          {
          for(k=i;k>0;k--)
               {
               stat=l*l+k*k;
               s=sqrt(stat);
               
               printf("l=%d\n",l);
               printf("k=%d\n",k );
               printf("stat=%d\n",stat );
               printf("%f\n",fmod(s,1.0) );
               if((fmod(s,1.0)==0.0) && (stat==n))
                   count++;
               }
          }
     printf("\nCount= %d",(count/2));
     return 0;
     }