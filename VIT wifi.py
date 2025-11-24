# WELCOME TO VIT BHOPAL WIFI SERVICE 
name = input("Enter your  name  :")
print(f"HELLO {name} welcome to our VIT WIFI  service \n")
number = input("Enter your registration number")
print(f" please verify again that is your registration number  is {number}\n")
answer = input("Enter yes or no ")
while(answer=="no" or len(number)!=10):
    number = input("Enter your registered  registration number  ")
    print(f" please verify again that is your registered mobile number is {number}")
    answer = input("Enter yes or no ")   

Batch = input("enter the year in which you joined our college ( 1 for 2022 , 2 for 2023 , 3 for 2024 , 4 for 2025 )")
 
username = (input("enter your provided USERNAME:"))


password = int(input("Enter your provided PASSWORD:"))
print(f"{name} verify that is your passowrd is {password}?")
reply = input("Enter yes or no ")
while(reply=="no"): 
    print(f"{name} verify that is your passowrd is {password}?")
    reply = input("Enter yes or no ") 

  
problem = input("Enter the type of problem are you facing ( 1 for network  , 2 for connection failed , 3 for speed , 4 for fortinet wasn't installed properly  , 5 for network problem in phone only  , else 0  ) ??")
if(problem=="1"):
    print(f"{name} To troubleshoot a Wi-Fi network problem, start by restarting your modem and router, checking all cable connections, and testing the connection on another device..")


elif(problem=="2"):
    print(f"{name} To fix a CONNECTION FAILED or Wi-Fi error, first restart your modem and router, then have your device forget and reconnect to the network .")

elif(problem=="3"):
    print(f"{name} restarting your modem and router, optimizing router placement in a central, open location, and reducing the number of devices connected.  ")

elif(problem=="4"):
    print(f"{name} Go to your device's Wi-Fi settings, find the problematic network name, and select FORGET or REMOVE and connect the network again")



elif(problem=="5"):
    print(f"{name} avoid models such as REDMI , REALME, GOOGLE PIXEL , IQOO and MOTOROLA , as they have certification conflicts ")

elif(problem=="0"):
    print(f"{name} come to CTS office with your id card.")
    








