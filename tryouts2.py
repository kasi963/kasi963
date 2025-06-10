#fortune telling.
import random
fortune=["you will do great in life",
         "you will never lack",
         "Allah will forever watch over you.",
         "ei, your life spoil o...",
         "omo, e too sure for you.. horh",
         "You will make your family proud in sha Allah"]
for fortunes in range(6):
 users_name=input("what is your name?")
 users_fortune=random.choice(fortune)
 print(f"dear {users_name}, {users_fortune}")
 if users_fortune==fortune[0]:
    print("good fortune for you!")
 elif users_fortune==fortune[1]:
    print("Good fortune for you!")
 elif users_fortune==fortune[2]:
    print("that is a good fortune! I pray it comes true!")
 elif users_fortune==fortune[3]:
    print("oops! bad fortune,try again")
 elif users_fortune==fortune[4]:
    print("oops! looks like you got the bad ones..try again")
 else:
    print('that is a good fortune! I pray it comes true!')
