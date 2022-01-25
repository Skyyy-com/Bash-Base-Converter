#!/usr/bin/python3

#By Skylar

print(" [1] binary to decimal ") 
print(" [2] decimal to binary ")
print(" [3] binary to hex ")
print(" [4] decimal to hex ")
print(" [5] hex to binary ")
print(" [6] hex to decimal ") 

print(" ")

choice = input("choice: ")


#choice 2

def decimalToBinary(val):
    if val >= 1:
 
        decimalToBinary(val // 2)
    
 
    print(val % 2, end = '')
 
if choice == "2":
    
    val = int(input("value: ")) 
     
    decimalToBinary(val)
    
    print(" ")


#choice 1

if choice == "1":
    val= input("value: ")
    real_val= int(val, 2)
    print(real_val)

#choice 3

def binaryToHex(val):
    real_val = hex(int(val, 2))
    print(real_val)
    

if choice == "3":
    binaryToHex(input("value: "))
   
#choice 4

def decimalToHex(val):
    real_val = hex(int(val))
    print(real_val)

if choice == "4":
    decimalToHex(input("value: "))

#choice 5

def hexToBinary(val):
    real_val = bin(int(val, 16))[2:].zfill(8)
    print(real_val)

if choice == "5":
    hexToBinary(input("value: "))

#choice 6

def hexToDecimal(val):
    real_val = int(val,16)
    print(real_val)

if choice == "6":
    hexToDecimal(input("value: "))
