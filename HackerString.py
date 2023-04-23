def string(s,sub):
        c=0
        for i in range(len(s)-len(sub)+1):
                if (s[i:i+len(sub)]==sub):
                        print(s[i:i+len(sub)])
                        c=c+1
    
        return c
s='ABCDCDC'
sub='CDC'
print(string(s,sub))
