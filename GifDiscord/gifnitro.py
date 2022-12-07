from base64 import urlsafe_b64decode
from http.client import REQUEST_ENTITY_TOO_LARGE
from optparse import check_builtin
import random
import string 
from  urllib import request

def gen():
    import random

    upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letter = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'

    numbtogen = input ('quantos eu gero: ')
    upper, lower, nums, = True, True, True, 
    all= ""

    if upper:
        all += upper_letter
    if lower:
        all += lower_letter
    if nums:
        all += digits

        lenght = 23
        amount = numbtogen

        for x in range(int(numbtogen)):
            nitro = ''.join(random.sample(all,lenght))
            print('discord.gif/' + nitro)


gen()
gen()
gen()
