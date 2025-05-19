#we want to build a programe to encrypt and decrypt a string of characters like we would usualy do in cybersecurity
import random
import string

print(help(string.ascii_letters))

chars = " " + string.ascii_letters + string.punctuation + string.digits #concartinating some string characters 

chars = list(chars) #lets typcast the string called chars into a list to make each character of the string a list item
key = chars.copy() #using the copy () method to copy the chars string and assign it to the key variable

random.shuffle(key)



#print(f'chars : {chars}')
#print(f'Keys: {key}')

#time to encrypt
plain_text = input("Enter a message to encrypt? ")
cipher_test = ""    #we want to replace our plain_test letters with keys. to do this, we need to interate over the plain_test
                    #and use a for loop to return the key in key above


#lets encrypt our message
for letters in plain_text:
   index = chars.index(letters) #we used the index() method of a list to get the first occuring index position of any letter within letters
   cipher_test += key[index]    #then used a string incrementer += to add the correspond key[index] to the empty string of cipher_test


print(f'plain Text is : {plain_text}')
print(f'cipher_test is : {cipher_test}')

#lets decrypt the cipher text

decrypted_test = "" #an empty string to act as colletor for our string

for letters in cipher_test:
   index = key.index(letters) #we used the index() method of a list to get the first occuring index position of any letter within letters
   decrypted_test += chars[index] 

print(f'decrypted test is : {decrypted_test}')




