# Enter your code here. Read input from STDIN. Print output to STDOUT
s=set(map(int,input().split(' ')))
n=int(input())
z='False'
a=0
for i in range(n):
    k=set(map(int,input().split(' ')))
    y=s.issuperset(k)
    if y=='True':
        if len(k)==len(s):
            for i in s:
                if i in s:
                    z='False'
                else:
                    z='True'
                    break
        else:
            z='True'
            break
                
                
    else:
      z='False'
      break
print(z)
