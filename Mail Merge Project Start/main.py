#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
for i in range(len(names)):
    name = names[i].strip("\n")
    names[i] = name

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
print(letter)



for name in names:
    final_letter = letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}", mode="w") as file:
        file.write(final_letter)
