# my-dogs.py

from dog import Dog

my_dog1 = Dog("Bubbles", "Maltipoo")
print (f"My dog's name is {my_dog1.name}, she is a {my_dog1.breed}")
my_dog1.bark()

my_dog2 = Dog("Bopper", "Corgi")
print (f"My dog's name is {my_dog2.name}, they are a {my_dog2.breed}")
my_dog2.sit()

my_dog3 = Dog("Buddy", "Jack Russell")
print (f"My dog's name is {my_dog3.name}, he is a {my_dog3.breed}")
my_dog3.roll_over()
