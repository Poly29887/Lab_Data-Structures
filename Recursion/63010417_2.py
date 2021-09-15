def palindrome(head,tail,s):
    if tail <= head :
      return 1
    else :
      if s[head] == s[tail]:
         c = 1
      else:
         c = 0
      return palindrome(head+1,tail-1,s)*c
    
         
output = ''
inp = input('Enter Input : ')
if palindrome(0,len(inp)-1,inp) == 0:
    output += 'is not palindrome'
elif palindrome(0,len(inp)-1,inp) == 1:
    output += 'is palindrome'

print(f'\'{inp}\' {output}')
