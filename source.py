
import os
import time
import urllib.request
print("plz wait")
time.sleep(0.2)
os.system("sudo apt-get install figlet")
os.system("clear")
os.system("figlet WizWopper ")
print(" ")
site = input("target website: (examp: https://www.google.com/) ")

htm = urllib.request.urlopen(site)
print(htm.read())
