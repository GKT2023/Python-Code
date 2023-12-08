def replace_Strip (str,word):
    new_str = str.replace(word,"")
    return new_str.strip()

str = "hi   Garima, how are you?  "
print(replace_Strip(str,"Garima"))