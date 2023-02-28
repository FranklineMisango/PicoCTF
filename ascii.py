#Final list for the final flag
final_list = "" 
#Reading from the test.txt that you generate after invoking nc
with open('test.txt', 'r') as file:
#We need to read each line since one line reps one ASCII code
    for line in file:
#Removing all the whitespaces
        line = line.strip()
#Changing each line to an integer to parse onto chr command
        ascii_code = int(line)
#Actualizing the alphanumeric code and parsing it into a liner final_list
        alphanumeric = chr(ascii_code)
        final_list += alphanumeric 
#Printing the final list and and stripping all whitespaces to finally answer     
final_list = final_list.strip()  
print(final_list)
