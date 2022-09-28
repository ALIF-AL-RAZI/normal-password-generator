import random
import string

lowerCase = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"
upperCase = string.ascii_uppercase  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = string.digits  # "0123456789"
symbols = string.punctuation  # "!@#$%&*()-+/\?"

allchr = lowerCase + upperCase + number + symbols
passLn = 8


def pass_gen():
    pswrd = "".join(random.sample(allchr, passLn))
    return pswrd


while True:
    x = pass_gen()
    print(x)


