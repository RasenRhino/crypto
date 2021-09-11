s="MWULNKBNHHUBWRHBXMHYAOUQVSNHWVZMCWNQWPLMAWGHIFJHDBQWNLNMWSWCUWAWCMCWDIBNLFZUEYLOENHYDDXHPZZCNKMADAKNQWMRMEJHGVOCMXKAWNKVFNHYDDXHPZZCNKMADAKZROYFOAAMLIFNFODSNHWVSNHWNYDMWWQJVOZFXMHOSXUONMWXDXTRYYZFQYPDZLFDNERWDGBUUQIUWASMAKFHHECBHVSNHWXMWUVNGVYWCMCCWDECBHJZUSVTECYPVOCCQBUWNKZIXLOYMUFRRUWAWCQJAHIFCIEZONLWVUWIIOTNWRIENKXZZLYVJRRNVVOCCRIEQIZZHNLLAFQYDBQWNLNZXNWCQXHOTMLNRMFQYQDFAYTPUAYVOTJNWCQJAHIFLUQMQJMRIGWXHMGWWHMFJCQOKCBLNOJFONRXLDIMPYQOFQUWXMWHROAWFBVEBYVNUCMHIHRLRIYNHWVZMGDFQYLHYULNLJZBVXOMUMRZHJFXVFNCWNBAYGDOCCRIEJHGVPJJWWMBYGJZRNVVEBYVNYNHWIMCOUVXUUQBGJAHKDXWHNERHJBUEYVHMLBLIQBNKZMKCODFHNRMQJXDIPDHGZDBNDIPQOPVZUUQBGJAH"
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 
def ic(x):
	dic={}
	for i in x:
		if(i not in dic.keys()):
			dic[i]=1
		else:
			dic[i]+=1
	num=int(0)
	for i in dic.keys():
		num+=(dic[i]*(dic[i]-1))
	l=len(x)
	final=(num)/((l*(l-1)))
	return final

# s="vptnvffuntshtarptymjwzirappljmhhqvsubwlzzygvtyitarptyiougxiuydtgzhhvvmumshwkzgstfmekvmpkswdgbilvjljmglmjfqwioiivknulvvfemioiemojtywdsajtwmtcgluysdsumfbieugmvalvxkjduetukatymvkqzhvqvgvptytjwwldyeevquhlulwpkt"
t=int(0)
count=int(0)
for i in range(0,6):
	temp=[]
	for j in range(count,len(s),5):
		temp.append(s[j])
	print(listToString(temp),end=':')
	print(ic(temp))
	count+=1




