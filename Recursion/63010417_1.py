def fatorial(n):
    if n == 0 or n == 1:
      return 1
    elif n>1:
      return fatorial(n-1)*n

inp = input('Enter Number : ')
print(f'{inp}! = {fatorial(int(inp))}')
