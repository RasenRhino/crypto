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
def count_occurence(source,find,l):
	count=int(0)
	for i in range(len(source)):
		temp=source[i:(i+(l))]
		if((temp)==(find)):
			count+=1
	return count

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


common_words=["ABUSE","ADULT","AGENT","ANGER","APPLE","AWARD","BASIS","BEACH","BIRTH"]

bigram={}
trigram={}
for i in range(len(s)):
	y=trigram.keys()
	tri=s[i:(i+5)]
	if(tri not in y):
		trigram[tri]=[count_occurence(s,tri,5),i]
	else:
		trigram[tri].append(i)

ind=trigram.keys()
most_occuring=[]
for i in ind:
	if(trigram[i][0]<3):
		continue
	else:
		most_occuring.append(i)
		print(i,end=',')
		print(trigram[i])		

alp=[]
alpha='A'
for i in range(0, 26):
    alp.append(alpha)
    alpha = chr(ord(alpha) + 1)
perm=permutations(alp,5)

for i in most_occuring:
	for j in perm:
		temp=decrypt(i,listToString(j),alp,trigram[i][1])
		if(listToString(temp) in common_words):
			print(j,end=' ')
			print(listToString(temp))
			


