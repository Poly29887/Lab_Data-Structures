def palindrome(head,tail,s):
    if tail <= head :
      return 1
    else :
      if s[head] == s[tail]:
         c = 1
      else:
         c = 0
      return palindrome(head+1,tail-1,s)*c
    

inp = str(input('Enter Input : '))
text_low = inp.lower()
l = []
output = ''
for e in text_low:
  if e not in '“”" !?.()+-*/’,;' :
   l.append(e)   

if palindrome(0,len(l)-1,l) == 0:
    output += 'is not palindrome'
elif palindrome(0,len(l)-1,l) == 1:
    output += 'is palindrome'

print(f'\'{inp}\' {output}')









