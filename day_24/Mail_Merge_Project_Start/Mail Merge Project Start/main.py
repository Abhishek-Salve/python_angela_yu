#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

name_list = []
with open('./Input/Names/invited_names.txt') as names_file:
    lines = names_file.readlines()
    for line in lines:
        name_list.append(line.strip())
print(name_list)


with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_lines = letter_file.readlines()
print(letter_lines)


for name in name_list:
    with open('./Output/ReadyToSend/{}.txt'.format(name + '_Letter'), "w+") as letter:
        for line in letter_lines:
            line = line.replace("[name]", name)
            line = line.replace("Angela", "Abhishek")
            letter.write(line)
