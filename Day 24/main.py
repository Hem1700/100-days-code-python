#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open ('./Input/Names/invited_names.txt') as file:
    name = file.read().split('\n')

with open('./Input/Letters/starting_letter.txt') as file:
    content = file.read()

for i in name:
    with open(f'./Output/ReadyToSend/starting_letter_{i}.txt', 'w') as file:
        new_letter = content.replace('[name]', f"{i}")
        file.write(new_letter)