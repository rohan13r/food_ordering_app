import random as rd

def generate_id():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    code = rd.choices([letters , numbers],weights =[5,10],k=7)
    return code