print(' *** Wind classification ***')
speed = float(input('Enter wind speed (km/h) : '))
if speed>=0 and speed <=51.99 :
    ans = 'Breeze'
elif speed>=52.00 and speed <=55.99:
    ans = 'Depression'
elif speed>=56.00 and speed <=101.99:
    ans = 'Tropical Storm'
elif speed>=102.00 and speed <=208.99:
    ans = 'Typhoon'
elif speed>=209 :
    ans = 'Super Typhoon'

print('Wind classification is '+ans+'.')