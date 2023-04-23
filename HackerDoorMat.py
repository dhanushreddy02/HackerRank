n=list(input().split(' '))
k=2*int(n[0])-2
y=int(n[1])
z=int(n[1])
d=(int(n[1]))-3
for i in range(0,int(n[0]),2):
    for j in range(y):
        if j==(y//2):
        
            for j in range(0,k):
                print(end="")
            k-=1
            for j in range(0,i+1):
                print('.|.',end="")
            y-=int(n[0])
        else:
            print("-",end="")
    if i==((int(n[0]))-1):
        
        for x in range(int(n[1])):
            if x==((int(n[0]))+2):
                print("Welcome",end="")
                x+=7
            else:
                print("-",end="")
        print()
        
        for i in range((int(n[0])),0,-2):
            for j in range(int(n[1]),0,-1):
                if j==d:
                    
                    for j in range(0,k):
                        print(end="")
                    k+=1
                    for j in range(0,i-2):
                        print('.|.',end="")
                    d+=3
                else:
                    print("-",end="")
            print()
    print()

   
