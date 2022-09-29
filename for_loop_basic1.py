

# # Basic 

for i in range(151):
    print(i)

# Multiples of Five 

for i in range (5, 1001,1):
    print(i*5)

# # Counting, the Dojo Way

def counting_dojo():
    for i in range (1,101,1):
        if i % 5 == 0 and i%10!= 0:
            print ("Coding")
        if i % 10 == 0:
            print ("Coding Dojo")
print (counting_dojo())

# # Whoa. That Sucker's Huge 

# minimum = 0
# maximum = 500000

sum = 0
for i in range(0,500000+1):
    if i % 2 == 1:
        sum = sum + i
print(sum)

# # Countdown by Fours 

def count_down_four():
    number = 2018
    while number > 0:
        print (number)
        number = number - 4
        
count_down_four()   

# # Flexible Counter

mult = 3
for i in range(3,10,1):
    if i % mult==0:
        print(i)