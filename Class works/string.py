# Strings in python

str1="srikamal"
str2="gummadi"
print(str1+str2)            #concatenation- joining 2 or more strings to gether
print(str1*3)               #repatition- repeating the string multiple times
print(str2[6])              #Indexing- accessing a particular character using its index
print(str2[1:3])            #Slicing- accessing a range of characters using their index
print("gummadi" in str2)    # Membership- checking if a substring is present in a string

# methods()
# case conversion methods

print(str1.upper())         #upper()- converts all characters to uppercase
print(str1.lower())         #lower()- converts all characters to lowercase
print(str1.capitalize())    #capitalize()- capitalizes the first character of the string
print(str1.title())         #title()- capitalizes the first character of each word in the string
print(str1.swapcase())      #swapcase()- converts uppercase to lowercase and vice versa

# alignment methods

print(str1.center(30,'*'))  #center()- centers the string with specified width and fill character
print(str1.ljust(35,'*'))   #ljust()- left justifies the string with specified width and fill character
print(str1.rjust(53,'*'))   #rjust()- right justifies the string with specified width and fill character
print('100'.zfill(30))      #zfill()-  fills the string with leading zeros to specified width

# searching and modifying methods   

print(str1.find('0'))       #find() - returns -1 if there is no letter
print(str1.rfind('a'))      #rfind()- used to find the last occurrence of a substring in a string. 
print(str1.index('k'))      #index() - if there is no letter it print Error
print(str1.rindex('k'))     #rindex()- Returns the position of the last occurrence of a substring,If not found → raises an error (ValueError)
print(str1.count('k'))      #count()- counts the number of occurrences of a substring

# replace & modify methods

print(str2.replace('s','*'))                        #replace()- replaces all occurrences of a substring with another substring
print(str1.translate(str1.maketrans('k','@')))      #translate()- translates characters based on a translation table
print(str2.maketrans('a','@'))                      #maketrans()- creates a translation table for use with translate()
print(len(str2))                                    #length()- returns the length of the string

# ordinal and character methods

print(ord('a'))             # max() and min()- returns the ASCII value of a character
print(max(str1))
print(min(str1))
print(chr(128579))          #char()- converts an ASCII value to its corresponding character
print(sorted(str2))         #sorted()- sorts the characters of the string in ascending order

# splitting and joining methods

print(str2.split('i'))          #split()- splits the string into a list of substrings based on a delimiter
print(str2.rsplit(' ',2))       # rsplit()- splits the string into a list of substrings from the right based on a delimiter and maxsplit
print(str2.splitlines())        #splitlines()- splits the string into a list of lines
print(str2.rpartition(' '))     #rpartition()- splits the string into a tuple of three parts from the right based on a separator
print(str2.partition(' '))      #partition()- splits the string into a tuple of three parts based on a separator
print(' '.join(['sri','kamal','gummadi'])) #join()- joins a list of strings into a single string with a specified separator

# whitespace removal methods

print(str2.strip())          #strip()- removes leading and trailing whitespace
print(str2.lstrip())         #lstrip()- removes leading whitespace
print(str2.rstrip())         #rstrip()- removes trailing whitespace
print('sri'.encode())        #encode()- encodes the string into bytes using a specified encoding
print(b'kamal'.decode())   #decode()- decodes bytes into a string using a specified encoding
print(str2.rstrip('gummadi'))   #rstrip()- removes the specified trailing characters

#string testing methods

print(str1.isalnum())       #isalnum()- checks if all characters are alphanumeric
print(str1.isalpha())       #isalpha()- checks if all characters are alphabetic
print(str2.isdecimal())     #isdecimal()- checks if all characters are decimal characters
print(str2.isdigit())       #isdigit()- checks if all characters are digits  
print(str2.islower())       #islower()- checks if all characters are lowercase
print(str2.isupper())       #isupper()- checks if all characters are uppercase
print(str2.istitle())       #istitle()- checks if the string is in title case       
print(str2.isspace())       #isspace()- checks if all characters are whitespace      
print(str2.startswith('l')) #startswith()- checks if the string starts with a specified substring
print(str2.endswith('h'))   #endswith()- checks if the string ends with a   specified substring
print("la" in str2)         # Membership- checking if a substring is present in a string 
print("ID" in str2)         # Membership- checking if a substring is present in a string (case-sensitive)