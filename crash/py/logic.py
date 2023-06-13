import random


num = 0

def random_crash():

    global num
    crash = random.randint(1, 1000)


    if crash <= 120:
        num = round(1.00)


    elif crash > 120 and crash <= 600:
        num = (round(random.uniform(1.01, 1.80), 2))


    elif crash > 600 and crash <= 800:
        num = (round(random.uniform(1.80, 5.00), 2))


    elif crash > 800 and crash <= 950:
        num = (round(random.uniform(5.00, 20.00), 2))


    elif crash > 950 and crash <= 990:
         num = (round(random.uniform(20.00, 100), 2))


    else:
     num = (round(random.uniform(100.00,500.00), 2))





