S = list(range(0, 256))  # 0-255

key = input("Enter the key_word: ").upper()
T = []  # keykeykey.....
for i in range(0, 256):
    T.append(key[i % len(key)])
print("Started S: " + str(S))
print("T:         " + str(T))

q = 0
for i in range(0, 256):
    q = (q + S[i] + ord(T[i])) % 256
    S[i], S[q] = S[q], S[i]  # Swap
print("New S:     " + str(S))
# print(S[1+81])#i=1 j=1+S[1]=82 swap j=81 i=1 k=S[127+1]

x = y = 0
K = []
for i in range(0, 256):
    x = (x + 1) % 256
    y = (y + S[x]) % 256  # x=1; S[x]=170 y=170; S[y]=81 ;
    S[x], S[y] = S[y], S[x]  # swap (x,y) s[x]=81 s[y]=170
    i = S[(S[x] + S[y]) % 256]  # i=81+170=251 S[251]=149
    K.append(i)
print("random K:  " + str(K))


# print("random K:  "+str(sorted(K)))# 2344688....

def enc_dic(mes,random_list):
    if mes=="Invalid value":
        return (mes+": Try again:")
    text = input("Enter the text"+mes)
    result = []
    for i in range(0, len(text)):
        result.append(chr(ord(text[i]) ^ random_list[i]))
    a = ''.join(result)
    return (a)

a = 0
while True:
    a = int(input("Please select:  \n1)Encript\n2)Decrypt\n3)Exit\n"))
    if a==3:break
    messig = " for encript: " if a == 1 else " for decrypt: " if a == 2 else "Invalid value"
    print(enc_dic(messig, K))
