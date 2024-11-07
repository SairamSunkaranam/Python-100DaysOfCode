#TODO: Create a letter using starting_letter.txt

with open("./Input/Letters/starting_letter.txt") as input_letter:
    letter_content = input_letter.read()
    print(letter_content)

#for each name in invited_names.txt

with open("./Input/Names/invited_names.txt") as names:
    invite_names = names.readlines()
    print(invite_names)

#Replace the [name] placeholder with the actual name.

for name in invite_names:
    new_name = name.strip()
    print(new_name)
    new_content = letter_content.replace("[name]", new_name)
    print(letter_content)

#Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/{new_name}.txt", mode="w") as output:
        output.write(new_content)
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp