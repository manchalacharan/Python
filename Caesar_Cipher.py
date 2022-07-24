'''
The example of encryption wae use by julius caesar.Casesar needed the provied instruction to his genral
but he didn't want his enenmies to learn his plans the message slipped into their hands
it provieds no protection against modern code breaking thechniques.
each letter the original message is shifted by 3 place.
Eg : A is become C,B is become D,y is become B,Z is become c. 
'''
message = input("Enter any name: ")
shift = int(input("Enter the shift value: "))

new_message = ""

for ch in message:
    if ch>= "a" and ch <= "z":
        pos = ord(ch) - ord("a")
        pos = (pos + shift)% 26
        new_char = chr(pos + ord("a"))
        new_message = new_message + new_char
    elif ch >= "A" and ch <= "Z":
        pos = ord(ch) - ord("A")
        pos = (pos + shift)% 26
        new_char = chr(pos + ord("A"))
        new_message = new_message + new_char
    else:
        new_message = new_message + ch

print("The shifted message is",new_message)
        
