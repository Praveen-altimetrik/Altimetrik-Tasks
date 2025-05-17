import random

def otp(length=6):
    otp_value = ''
    for i in range(length):
        otp_value += str(random.randint(0,9))
    return otp_value


result = otp()
print(result)