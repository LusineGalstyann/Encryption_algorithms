text = input("Enter the text: ").replace(" ", "")
key = int(input("Enter the key: "))

while len(text) % key != 0:
    text += "z"
def create_list(t, k):
    t_list = []
    for i in range(0, len(t), k):
        t_list.append(list(t)[i:i + k])
    return (t_list)
def make_strin(l):
    new_text = ''
    new_text = ''.join(l)
    return (new_text)
def enc_dic(k, l):
    new_list = []
    for i in range(0, k):
        for j in range(int(len(text) / k)):
            new_list.append(l[j][i])
    return (new_list)

enc_text = make_strin(enc_dic(key, create_list(text, key)))
print("Encrypted text is:  "+str(enc_text))
dec_text = make_strin(enc_dic(int(len(text) / key), create_list(enc_text, int(len(text) / key))))
print("Descrypted text is: "+str(dec_text))
# Computer Systems and Informatics Department
