#include<stdio.h>
void main()
{
int n,i,x[100],y[100];
float xpred,xbarr=0,ybarr=0,xbar,ybar,p,q,r,g,z=0,f=0,b1,b0,ypred;
printf("Enter the number of co-ords:\n");
scanf("%d" ,&n);
printf("Enter co-ords: ");
for(i=0;i<n;i++)
{
scanf("%d %d" ,&x[i],&y[i]);
}
printf("Enter co-ord prediction of x: ");
scanf("%f" ,&xpred);
for(i=0;i<n;i++)
{
xbarr=xbarr+x[i];
ybarr=ybarr+y[i];
}
xbar=xbarr/n;
ybar=ybarr/n;
for(i=0;i<n;i++)
{
p=x[i]-xbar; // xi-xbar(1)
q=y[i]-ybar; //yi-ybar(2)
r=p*q; 	//1*2(3)
z=z+r; 	//sum3
g=p*p; 	//square1(4)
f=f+g; 	//sum4
b1=z/f; 	//sum3/sum4(b1)
b0=ybar-b1*xbar; //ybar-b1*xbar(b0)
ypred=b0+b1*xpred; //b0+b1*x(ypred)
}
printf("ypred is: %.2f \n" ,ypred);
}


