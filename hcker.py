from typing import List, Tuple

def palindromeChecker(s, startIndex, endIndex, subs):
    result = ""
    loop = len(subs)
    
    for i in range(loop):
        
        sub_string = s[startIndex[i]: endIndex[i]+1]
        allowed_subs = subs[i]
        print("all",sub_string)
        
        sol = can_be_palindrome(sub_string,allowed_subs)
        
        result+=sol

    return result


def can_be_palindrome(s:str,n:int)-> str:

    freq = {}
    for i in s:
        freq[i] = freq.get(i,0) + 1

    odd_count = 0
    for v in freq.values():
        if v % 2 == 1:
            odd_count += 1
    return str(int(odd_count <= n))
 
	# s = list(s)
	# x = len(s)
	# cc = 0

	# for i in range(x//2):
	# 	if(s[i]== s[x-i-1]):
	# 		continue
	# 	cc+= 1

	# 	if(s[i]<s[x-i-1]):
	# 		s[x-i-1]= s[i]
	# 	else:
	# 		s[i]= s[x-i-1]
	# 	print(cc)
 
     
 
	
	# return str(int(odd_count <= n))
	
# # Driver code
s = "cdecd"
startIndex = [0,0,0,0]
endIndex = [0,1,2,3]
subs = [0,1,1,0]


sol = palindromeChecker(s, startIndex, endIndex, subs)
res= can_be_palindrome(s,3)
print(sol)



# def can_rearrange_to_palindrome(s: str, queries: List[Tuple[int, int, int]]) -> List[bool]:
#     def check(l: int, r: int, k: int) -> str:
#         # Count the frequency of each character in the substring
#         freq = {}
#         for i in range(l, r + 1):
#             freq[s[i]] = freq.get(s[i], 0) + 1

#         # Check if there are more than k characters with an odd frequency
#         odd_count = 0
#         for v in freq.values():
#             if v % 2 == 1:
#                 odd_count += 1
#         return odd_count <= k

#     return [check(l, r, k) for l, r, k in queries]
    
    

# queries = [(0, 5, 1), (0, 5, 2), (0, 5, 3)]
# print(can_rearrange_to_palindrome("abcba", queries))  # Output: [True, True, False]