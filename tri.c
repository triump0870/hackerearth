#include<stdio.h>
#include<math.h>
int main()
     {
     int i,n,k,l,stat,count=0;
     
     printf("\nEnter the value of 'n': ");
     scanf("%d",&n);
     i = sqrt(n);
     printf("%d\n",i );
     for(l=i;l>0;l--)
          {
          for(k=i;k>0;k--)
               {
               stat=l*l+k*k;
               double f = sqrt(stat);
               printf("%lf\n",f );
               printf("%f\n",fmod(f,1) );
               if(fmod(f,1.0)==0 && stat<n)
                   count++;
               }
         }
    printf("\nCount= %d\n",count);
    return 0;
    }