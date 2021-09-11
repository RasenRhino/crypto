from itertools import permutations
s="MWULNKBNHHUBWRHBXMHYAOUQVSNHWVZMCWNQWPLMAWGHIFJHDBQWNLNMWSWCUWAWCMCWDIBNLFZUEYLOENHYDDXHPZZCNKMADAKNQWMRMEJHGVOCMXKAWNKVFNHYDDXHPZZCNKMADAKZROYFOAAMLIFNFODSNHWVSNHWNYDMWWQJVOZFXMHOSXUONMWXDXTRYYZFQYPDZLFDNERWDGBUUQIUWASMAKFHHECBHVSNHWXMWUVNGVYWCMCCWDECBHJZUSVTECYPVOCCQBUWNKZIXLOYMUFRRUWAWCQJAHIFCIEZONLWVUWIIOTNWRIENKXZZLYVJRRNVVOCCRIEQIZZHNLLAFQYDBQWNLNZXNWCQXHOTMLNRMFQYQDFAYTPUAYVOTJNWCQJAHIFLUQMQJMRIGWXHMGWWHMFJCQOKCBLNOJFONRXLDIMPYQOFQUWXMWHROAWFBVEBYVNUCMHIHRLRIYNHWVZMGDFQYLHYULNLJZBVXOMUMRZHJFXVFNCWNBAYGDOCCRIEJHGVPJJWWMBYGJZRNVVEBYVNYNHWIMCOUVXUUQBGJAHKDXWHNERHJBUEYVHMLBLIQBNKZMKCODFHNRMQJXDIPDHGZDBNDIPQOPVZUUQBGJAH"

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 
def stringToList(string):
    list1=[]
    list1[:0]=string
    return list1
def decrypt(ei,key,al,ind):
    a=[]
    j=int(0)
    keylen=len(key)
    for i in range(len(ei)):
        eindex=al.index(ei[i])
        kindex=(ind+i)%keylen
        temp=(eindex-(al.index(key[kindex])))%26
        a.append(al[temp])
        j+=1
        if(j>(len(key)-1)):
            j=0
    return a
alp=[]
alpha='A'
for i in range(0, 26):
    alp.append(alpha)
    alpha = chr(ord(alpha) + 1)
print(listToString(decrypt(s,"MJUDV",alp,0)))