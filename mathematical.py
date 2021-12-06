import requests

val = input("Enter \"add\" or \"subtract\": ")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
URL = "http://127.0.0.1:5000/" + val + "/" + num1 + "/" + num2

r = requests.get(url=URL)
print(r.json())