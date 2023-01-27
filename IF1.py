alien_color = 'green'
if alien_color == 'green':
 print("You just earned 5 points!")

alien_color = 'green'
if alien_color == 'green':
 print("You just earned 5 points!")
else:
 print("You just earned 10 points!")

alien_color = 'red'
if alien_color == 'green':
 print("You just earned 5 points!")
elif alien_color == 'yellow':
 print("You just earned 10 points!")
else:
 print("You just earned 15 points!")

age = 17
if age < 2:
 print("You're a baby!")
elif age < 4:
 print("You're a toddler!")
elif age < 13:
 print("You're a kid!")
elif age < 20:
 print("You're a teenager!")
elif age < 65:
 print("You're an adult!")
else:
 print("You're an elder!")

 favorite_fruits = ['blueberries', 'salmonberries', 'peaches']
if 'bananas' in favorite_fruits:
 print("You really like bananas!")
if 'apples' in favorite_fruits:
 print("You really like apples!")
if 'blueberries' in favorite_fruits:
 print("You really like blueberries!")
if 'kiwis' in favorite_fruits:
 print("You really like kiwis!")
if 'peaches' in favorite_fruits:
 print("You really like peaches!")

 
numbers = list(range(1,10))
for number in numbers:
if number == 1:
 print("1st")
elif number == 2:
 print("2nd")
elif number == 3:
 print("3rd")
else:
 print(f"{number}th")