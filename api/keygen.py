import random

def deviceID():
    e1 = random.choice('abcdefghij')
    e2 = str(random.randint(100, 999))
    e3 = random.choice('abcdefwxyz')
    e4 = random.choice('klmnopqrstuv')
    e5 = str(random.randint(100, 999))
    e6 = e1 = random.choice('abcdefghij')
    final_element = e1+e2+e3+"-"+e4+e5+e6
    return final_element

def userKEY():
    e1 = random.choice('abcdefghij')
    e2 = str(random.randint(1, 1000))
    e3 = random.choice('abcdefwxyz')
    e4 = str(random.randint(1, 1000))
    e5 = random.choice('klmnopqrstuv')
    e6 = str(random.randint(1, 1000))
    final_element = e1+e2+e3+"-"+e4+e5+e6
    return final_element