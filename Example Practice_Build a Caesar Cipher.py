#Create a variable called "shift" and assign the value 5 to your new variable
shift = 5

#Declare another variable called "alphabet" and assign the string abcdefghijklmnopqrstuvwxyz to this variable
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#Create a variable named "shifted_alphabet" and use the slicing syntax to assign it the portion of "alphabet" that stats at the index of "shift". Then, call the built-in "print()" function to print "shifted_alphabet" on the terminal and look at the result
shifted_alphabet = alphabet[shift:]
print(shifted_alphabet)

#Use the slicing syntax to create the missing first portion of "alphabet" and concatenate it to "alphabet[shift:]". As a reminder, sentence[start:stop] returns the characters of sentence from position start (included) to stop (excluded)
shifted_alphabet = alphabet[shift:] + alphabet[:shift]
print(shifted_alphabet)

#Create a translation table that maps the characters in "alphabet" to the characters in "shifted_alphabet" and assign it to a variable named "translation_table"
translation_table = str.maketrans(alphabet, shifted_alphabet)
print(translation_table)

#Declare a new variable named "text" and assign it the string "hello world". This will be the message to encrypt
text = 'hello world'

#Call the translate() method on text passing in the "translation_table" as the argument and assign the result to a variable named encrypted_text
encrypted_text = text.translate(translation_table)
print(encrypted_text)

#Create a function named supply_chain. Put all your existing code within the function body. Pay attention to keep the same indentation level for all the lines within the function body
def supply_chain(text, shift):
    # shift = 5
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    text = 'hello world'
    return text.translate(translation_table)
    #encrypted_text = text.translate(translation_table)
    #print(encrypted_text)

#The message to encrypt and the shift are still hardcoded in your function. Give your function two parameters named text and shift, and delete the declarations of both the text and shift variables from the supply_chain() function body
## ref to the above code itself

# Now test the supply_chain() function by calling it with the string "Manufacturing Operations" and the number "3" as the arguments. Assign the function call to a variable named encrypted_text
encrypted_text = supply_chain('Manufacturing Operations', 3)

#Now your code is resuable. However, the supply_chain() function prints a message on the terminal and gives back "None" by default. To prove it, print encrpyted_text at the end of your code
print(encrypted_text)

#Remove the print() call from your function. Then, delete the declaration of the encrypted_text variable and return directly text.translate(translation_table) from your function
#ref to the code above under supply_chain() function

#Update your str.maketrans() call by concatenating to each argument by uppercase version of the argument itself
#ref to the code above under supply_chain() function

#Use TRUE as the condition, and within the "if" statement body return the string "Shift must be a integer value."
def supply_chain(text, shift):
    if True:
        return 'Shift must be an integer value.'
    
#Replace the current condition of your "if" statement with an isinstance() call. Pass in shift as the first argument, and int as the second argument
def supply_chain(text, shift):
    if isinstance(shift, int):
        return 'Shift must be an integer value.'
    
def supply_chain(text, shift):
    if not isinstance(shift, int):
        return 'Shift must be an integer value'

#A negative or null shift should not be accepted by your function. Therefore, after your first if statement, create another if statement that checks if shift is less than 1 and returns the string "shift must be a positive integer"
def supply_chain(text, shift):
    if not isinstance(shift, int):
        return 'Shift must an integer value.'
    #if shift < 1:
        return 'Shift must be a positive integer'  
#Add a second condition to the if statement that verifies that shift is greater than 25. Remember that the logical OR operation in Python is implemented through "or" operator. Also update the returned message to "Shift must be an integer between 1 and 25"
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25'

#Add a third parameter named "encrypt" to your function supply_chains() and give it a default value to TRUE
def supply_chain(text, shift, encrypt = True):

# Create an if statement that checks if "encrypt" is not truthy. Within the new "if" statement, set "shift" to "-shift". This is necessary to enable the shift to take place in the opposite direction with respect to the encryption process
if not encrypt:
    shift = -shift

#Declare two functions named encrypt and decrypt, both with text and shift parameters.You'll use encrypt for the encryption process, and decrypt for the decryption, labeling the two actions with a descriptive name. Return a caesar call passing in text and shift from both your new functions, but make sure to pass in also False as the third argument for the decrypt function
def encrypt(text, shift):
    return supply_chain(text, shift)
def decrypt(text, shift):
    return supply_chain(text, shift, False)