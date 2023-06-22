#!/usr/bin/env python
# coding: utf-8

# In[47]:


'''Individual Programming Assignment 2

70 points

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.
    5 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''

    
    new_message = ''
    
    #If a Space is Entered
    if letter == " ":
        
        new_message += " "
        
    #If a letter is Entered
    else:
        
        #Finding Initial Position of Letter
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        counter = 0
        for i in alphabet:
            if i != letter:
                counter += 1
            else:
                position_of_letter = counter
                break

        #Getting Shifted Letter
        
        new_position = (position_of_letter + shift) % 26
        new_message += alphabet[new_position]
        
    return new_message


# In[54]:


def caesar_cipher(message, shift):
    '''Caesar Cipher.
    10 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    
    new_message = ''
    
    for letter_within_message in message:
        #If a Space is Entered
        if letter_within_message == " ":            
            new_message += " "

        #If a letter is Entered
        else:

            #Finding Initial Position of Letter
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            counter = 0
            for i in alphabet:
                if i != letter_within_message:
                    counter += 1
                else:
                    position_of_letter = counter
                    break

            #Getting Shifted Letter

            new_position = (position_of_letter + shift) % 26
            new_message += alphabet[new_position]
            
    return new_message


# In[80]:


def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.
    10 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''

    new_message = ''
    
    #If a Space is Entered
    if letter == " ":        
        new_message += " "
        
    #If a letter is Entered
    else:
        
        #Finding Initial Position of Letter
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        counter = 0
        for i in alphabet:
            if i != letter:
                counter += 1
            else:
                position_of_letter = counter
                break
        
        #Getting Position of letter_shift
        counter = 0
        for j in alphabet:
            if j != letter_shift:
                counter += 1
            else:
                position_of_letter_shift = counter
                break
        
        
        
        #Getting Shifted Letter

        new_position = (position_of_letter + position_of_letter_shift) % 26
        new_message += alphabet[new_position]
        
    
            
    return new_message


# In[72]:


def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''

    new_message = ''
    
    #Check if Key is as Long as the message and make neccessary adjustments
    if len(message) > len(key):
        key = key * 2 * (len(message) - len(key))
        key = key[0:len(message)]

    #For counting which position we're dealing with
    instance_counter = 0
    
    for letter_within_message in message:
        
        
        #If a Space is Entered
        if letter_within_message == " ":
            
            new_message += " "
            
            instance_counter += 1
            
        #If a Letter is Entered 
        else:
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            counter = 0
            key_counter = 0
            
            message_letter = message[instance_counter]
            key_letter = key[instance_counter]
            
            #Position of Letter From Message
            for i in alphabet:
                if i != message_letter:
                    counter += 1
                else:
                    position_of_letter = counter
                    break
            
            #Position of Corresponding Letter from Key
            for j in alphabet:
                if j != key_letter:
                    key_counter += 1
                else:
                    position_of_shift = key_counter
                    break
                   
            #Finding New Position
            new_letter_position = (position_of_letter + position_of_shift) % 26
            new_message += alphabet[new_letter_position]
            instance_counter += 1
        
                
    return new_message



# In[74]:


def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''

    #Check if length of the message is a multiple of the shift and adjust accordingly
    
    while len(message) % shift != 0:
        message = message + "_"
    
    #Constructing Encoded Message
    
    index = 0
    new_message = ''
    
    for i in message:
        new_position = (index // shift) + (len(message) // shift) * (index % shift)
        new_message += message[new_position]
        index += 1
        
    return new_message


# In[78]:


def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''

    #Create a Placeholder to Place the Letters in the Correct Order Eventually
    placeholder = "*" * len(message)
    placeholder_list = list(placeholder)
    
    
    #Initialize Needed Variables
    index = 0
    amount_of_columns = len(message) // shift
    amount_of_rows = shift
    
    #Go Through Each Letter in the Encrypted Message (by going through each row of each column)

    for column in range(amount_of_columns):
        
        for current_row in range(amount_of_rows):
            
            original_position = (current_row * (amount_of_columns) + column)
            placeholder_list[original_position] = message[index]
            
            index += 1
    
    #Place letters back into a STRING 
    original_word = ''
    
    for element in placeholder_list:
        
        original_word += element
    
    return(original_word)

