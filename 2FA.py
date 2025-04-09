import pyotp
import random
key_2FA = ""

def key_gen():
    global key_2FA
    length = 16
    letters=["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z"]
    digits=["2","3","4","4","6","7"]
    
    random_charakters = letters + digits
    for i in range(length):
       result_str = "".join(random.choice(random_charakters))
       key_2FA=key_2FA+result_str
    print("Randomly generated shared secret ", length, "is:", key_2FA)
    query_2FA()


def test_2FA():
    
    input_totp = input("Please enter your 2FA code: ")
    global key_2FA
    totp = pyotp.TOTP(key_2FA)
    if totp.now() == input_totp:
       print("Verification successful.")
    
    else: 
        print("The entered 2FA code is invalid.")
    option()


def query_2FA():
    global key_2FA
    totp = pyotp.TOTP(key_2FA)      
    print("Your current TOTP code is: " ,totp.now())
    option()

def option():
    global key_2FA
    option = input ("Would you like to generate a new shared secret or test an existing one? (1 = generate, 2 = test): ")
    if option == "1":
        key_gen()
    else:
        key_2FA = input("Geben sie ihr Shared Secret ein: ")
        test_2FA()

option()  

