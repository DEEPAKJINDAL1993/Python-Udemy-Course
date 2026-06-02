template = open("./Input/Letters/starting_letter.txt",'r')
email = template.readlines()

with open("./Input/Names/invited_names.txt",'r') as f:
    names = f.read().splitlines()
print(names)

with open("./Input/Letters/starting_letter.txt",'r') as template:
    new_email = template.read()
    for name in names:
        file_name = "./Output/ReadyToSend/Invitation_letter_" + name + ".txt"
        with open(file_name,'w') as out:
            updated_email = new_email.replace("[name]",name)
            print(updated_email)
            out.write(updated_email)


