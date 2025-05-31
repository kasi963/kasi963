def prime_num(number):
    is_prime = True
    for i in range(2,number):
         if number % i == 0:
             is_prime = False
    if is_prime:
        print("it is a prime number")
    else:
        print("it is not a prime number")
number_checker=int(input("Please enter a number\n"))
prime_num(number_checker)