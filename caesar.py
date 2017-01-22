def alphabet_position(letter):
    if letter.isupper()== True:
        return int((ord(letter)-ord("A")))
    elif letter.islower()== True:
        return int((ord(letter)-ord("a")))

def rotate_character(char, rot):
    if char.isalpha()==True:
        if char.isupper()== True:
            rot_char=int(ord("A"))+(rot+alphabet_position(char))%26
            return chr(rot_char)
        elif char.islower()== True:
            rot_char=int(ord("a"))+(rot+alphabet_position(char))%26
            return chr(rot_char)
    else:
        return char

def encrypt(text, rot):
    new_text=''
    for i in range(len(text)):
        new_text=new_text+rotate_character(text[i], rot)
    return new_text
