import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
         'p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','*']
print("welcome to pypassword generator")
nr_letters=int(input('how many letters?'))
nr_numbers=int(input('how many numbers?'))
nr_symbols=int(input('how many symbols?'))
password=[]
for char in range(nr_letters):
   password.append(random.choice(letters))
for number in range(nr_numbers):
    password.append(random.choice(numbers))
for symbol in range(nr_symbols):
    password.append(random.choice(symbols))
random.shuffle(password)
password="".join(password)
print(f'your password is {password}')


