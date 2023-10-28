key = int(input("Enter the key: "))
text = input("Enter the text: ")
encrypt_or_decrypt = int(input("If you want encrypt text select 1, if you want decrypt text select 2: "))

if encrypt_or_decrypt == 2:
    key = -key
enc_text = ""
for i in text:
    if ord(i) != 32:
        if i.isupper():
            enc_text += chr((ord(i) - 65 + key) % 26 + 65)
        elif i.islower():
            enc_text += chr((ord(i) - 97 + key) % 26 + 97)
    else:
        enc_text += " "
print(enc_text)
