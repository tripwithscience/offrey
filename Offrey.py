#!/usr/bin/python
import random
print("===dance like no one is watching ===")

symbols = "[]{}()?/\|<>@&%*$~';:._-#...!"
numbers = "0123456789"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
word = "4bcd3fgh1jklmn0pqrstuvwxy2"
hint = "wizard"
print("[+]generating password...")
print("[+]encrypt like everyone is...")


encrypt = symbols + numbers + word + lower + upper + hint

length = 32
password = "".join(random.sample(encrypt, length))
print(password)
