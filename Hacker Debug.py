'''a=input().split(' ')
print(a)
c='aeiou'
co=0
f=0
for i in a:
    j=str(i)
    for k in j:
        if k in c:
            print(k,end="")
            co+=1
    print(co)
    if co%2==0:
        f+=2
    else:
        f+=1
    print(co,f)
    co=0
print(f)'''
n = int(input())
words = input().split(' ')
z=['a', 'e', 'i', 'o', 'u', 'y']
score = 0
for word in words:
    num_vowels = 0
    for letter in word:
        if letter in z:
            num_vowels += 1
    
    if num_vowels % 2 == 0:
        score += 2
    else:
        score+=1
    print(num_vowels,score)
print(score)



        
    
