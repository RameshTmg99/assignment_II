""" Write a Python program to get a string made of the first 2 and the last 2
chars from a given a string. If the string length is less than 2, return
“Empty String”.
Sample String : ‘HelloworLD’
Expected Result : 'HeLD'
Sample String : 'a3'
Expected Result : 'a3a3'
Sample String : 'w'
Expected Result : ‘Empty String’ """

#code

string = str(input("Enter the string: "))
if(len(string) < 2):
    print("Empty String")
else:
    first = string[:2]
    second = string[-2:]
    print(first+second)
    
    
