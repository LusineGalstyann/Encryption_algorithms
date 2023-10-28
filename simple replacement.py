key_text = input("Enter the any text: ").lower()
#State engineering university of Armenia
key1 = ""
for i in key_text:
    if i not in key1 and ord(i) != 32:
        key1 += i

alphabet = "abcdefghijklmnopqrstuvwxyz"
key2=alphabet
for i in key1:
    if i in alphabet:
        key2=key2.replace(i, "")


fullkey = key1 + key2

text = input("Enter the text for encryption: ").lower()
enc_text = ""

for i in text:
    if ord(i) != 32:
        index = ord(i) - 97
        enc_text += str(fullkey[index])
    else:
        enc_text += " "
print("Encrypt : " + enc_text)





dtext=input("Enter text for decryotion: ")
dec_text=''
for i in dtext:
    if ord(i) != 32:
        index=fullkey.find(i)
        dec_text+=alphabet[index]
    else:
        dec_text += " "
print("Decrypt : " + dec_text)