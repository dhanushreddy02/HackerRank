def print_formatted(number):
        z=len(bin(number).replace('0b',''))
        l=['a','b','c','d','e','f']
        j=''
        for i in range(1,number+1):
                a=str(i).rjust(z)
                b=oct(i).replace('0o','').rjust(z)
                c=hex(i).replace('0x','').rjust(z)
                
                d=bin(i).replace('0b','').rjust(z)
                for i in c:
                        if i in l:
                                j+=(chr(ord(i)-32))
                        else:
                                j+=i
                print(a,b,j,d)
                j=''
        
number=21
print(print_formatted(number))
