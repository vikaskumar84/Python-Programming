for n in range(1,100):
     f=1
     for i in range(2,(n//2)+1):
         if n%i==0:
             f=0
             break
     if f==1 and n>1:
         print(n)
