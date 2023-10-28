key_text = input("Enter the any text: ").lower()
# State engineering university of Armenia good brooms sweep clean

key_list = []
for i in key_text:
    if i not in key_list and ord(i) != 32 and ord(i) != 106:
        key_list.append(i)
for i in range(97, 123):
    key_list.append(chr(i)) if chr(i) not in key_list and i != 106 else ''

key_matrix = []
for i in range(0, 25, 5):
    key_matrix.append(key_list[i:i + 5])

for i in range(5):
    for j in range(5):
        print(key_matrix[i][j], end=" ")
    print("")

text = input("Enter the text for encryption: ").lower().replace(' ', '').replace('j', 'i')
# good brooms sweep clean
for i in range(0, len(text), 2):
    if text[i] == text[i + 1]:
        text = text[:i + 1] + "z" + text[i + 1:]

text = text + "z" if len(text) % 2 == 1 else text
print("Modimy text is: " + str(text))


def x_y(text):
    x = []
    y = []
    for t in text:
        for i in range(5):
            for j in range(5):
                if t == key_matrix[i][j]:
                    x.append(i)
                    y.append(j)
    return x, y


t = list(text)
x, y = x_y(text)


def change(messige, ind):
    global t
    if messige == "same row":
        if y[ind] == 4:
            y[ind] = -1
        t[ind] = key_matrix[x[ind]][y[ind] + 1]
    elif messige == "same colum":
        if x[ind] == 4:
            x[ind] = -1
        t[ind] = key_matrix[x[ind] + 1][y[ind]]
    elif messige == "diagonal":
        t[ind] = key_matrix[x[ind]][y[ind + 1]]
        t[ind + 1] = key_matrix[x[ind + 1]][y[ind]]


a = ''
for i in range(0, len(text), 2):
    if x[i] == x[i + 1]:
        a = "same row"
        change(a, i + 1)
    elif y[i] == y[i + 1]:
        a = "same colum"
        change(a, i + 1)
    else:
        a = "diagonal"
    change(a, i)
encrypt_text = ''.join(t)
print("Encrypt text is: " + str(encrypt_text))

dis_text = input("Enter the text for descryption: ")
dt = list(dis_text)

x, y = x_y(dis_text)


def d_change(messige, ind):
    if messige == "same row":
        if y[ind] == 0:
            y[ind] = 5
        dt[ind] = key_matrix[x[ind]][y[ind] - 1]
    elif messige == "same colum":
        if x[ind] == 0:
            x[ind] = 5
        dt[ind] = key_matrix[x[ind] - 1][y[ind]]
    elif messige == "diagonal":
        dt[ind] = key_matrix[x[ind]][y[ind + 1]]
        dt[ind + 1] = key_matrix[x[ind + 1]][y[ind]]


a = ''
for i in range(0, len(dis_text), 2):
    if x[i] == x[i + 1]:
        a = "same row"
        d_change(a, i + 1)
    elif y[i] == y[i + 1]:
        a = "same colum"
        d_change(a, i + 1)
    else:
        a = "diagonal"
    d_change(a, i)

last = dt[len(dt) - 1]
if last == "z":
    dt.pop()
decrypt_text = ''.join(dt)
print("decrypt text is: " + str(decrypt_text))
