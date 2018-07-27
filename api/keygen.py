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

def channelID():
    e1 = random.choice('abcdefghij')
    e2 = str(random.randint(100, 999))
    e3 = random.choice('abcdefwxyz')
    e4 = random.choice('klmnopqrstuv')
    e5 = str(random.randint(100, 999))
    e6 = e1 = random.choice('abcdefghij')
    e7 = random.choice('abcdefghij')
    e8 = str(random.randint(100, 999))
    e9 = random.choice('abcdefwxyz')
    e10 = random.choice('klmnopqrstuv')
    e11 = str(random.randint(100, 999))
    e12 = e1 = random.choice('abcdefghij')
    final_element = e1+e2+e3+e4+e5+e6+e7+e8+e9+e10+e11+e12
    return final_element

def sensorID():
    e1 = random.choice('abcdefghij')
    e2 = str(random.randint(100, 999))
    e3 = random.choice('abcdefwxyz')
    e4 = random.choice('klmnopqrstuv')
    e5 = str(random.randint(100, 999))
    e6 = e1 = random.choice('abcdefghij')
    e7 = random.choice('abcdefghij')
    e8 = str(random.randint(100, 999))
    e9 = random.choice('abcdefwxyz')
    e10 = random.choice('klmnopqrstuv')
    e11 = str(random.randint(100, 999))
    e12 = e1 = random.choice('abcdefghij')
    final_element = e1+e2+e3+e4+e5+e6+e7+e8+e9+e10+e11+e12
    return final_element