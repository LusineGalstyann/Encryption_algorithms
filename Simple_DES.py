def P(n, l):
    if n == 10:
        ind = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
    elif n == 8:
        ind = [5, 2, 6, 3, 7, 4, 9, 8]
    elif n == "IP":
        ind = [1, 5, 2, 0, 3, 7, 4, 6]
    elif n == "IP_1":
        ind = [3, 0, 2, 4, 6, 1, 7, 5]
    elif n == "EP":
        ind = [3, 0, 1, 2, 1, 2, 3, 0]
    elif n == 4:
        ind = [1, 3, 2, 0]
    result = []
    for i in range(0, len(ind)):
        result.append(l[ind[i]])
    return (result)
def LS(num, l):
    num = num % 5
    return (l[num::] + l[:num:])
def Sbox(side, Box_num):
    x = int((str(side[0]) + str(side[-1])), 2)
    y = int((str(side[1]) + str(side[2])), 2)
    print("Sbox indexs are:   " + str(x) + " " + str(y))
    return (Box_num[x][y])
def Fk(k, l, r):
    xor_p1 = P("EP", r)
    print("After EP:          " + str(xor_p1))
    xor_p2 = k
    fxor = []
    print("K is----------------------------------------------- "+str(k))
    for i in range(8):
        fxor.append(xor_p1[i] ^ xor_p2[i])
    print("After xor:         " + str(fxor))
    l2 = fxor[:4:]
    r2 = fxor[4::]
    a, b = Sbox(l2, S0), Sbox(r2, S1)
    print("The values of Sbox:" + str(a) + " " + str(b))
    bin_value = str('{0:02b}'.format(a) + '{0:02b}'.format(b))
    print("In binar:          " + str(bin_value))
    p4 = P(4, bin_value)
    print("After P4:          " + str(p4))
    fxor = []
    for i in range(4):
        fxor.append(int(p4[i]) ^ l[i])
    print("Finaly xor:        " + str(fxor))
    return (fxor)
def key_generation(a):
    step_1 = P(10, a)
    print("After P10:         " + str(step_1))
    part_1 = step_1[:5:]
    part_2 = step_1[5::]
    print("Part 1 and part 2: " + str(part_1) + " " + str(part_2))
    part_1 = LS(1, part_1)
    part_2 = LS(1, part_2)
    k1 = P(8, (part_1 + part_2))
    print("Key 1:             " + str(k1))
    k2 = P(8, (LS(2, part_1) + LS(2, part_2)))
    print("Key 2:             " + str(k2))
    return (k1, k2)
def Sdes(k1, k2, p):
    ip = P("IP", p)
    print("IP:                " + str(ip))
    l1 = ip[:4:]
    r1 = ip[4::]
    print("l1 and r1 are:     " + str(l1) + str(r1))
    fk_1 = Fk(k1, l1, r1)
    fk_1, r1 = r1, fk_1  # swich //r-r1 l-fk_1
    print("After swich:       " + str(fk_1 + r1))
    print("////////////    Part 2    ////////////////")
    fk_2 = Fk(k2, fk_1, r1)
    print("After Second part: " + str(fk_2 + r1))
    a = P("IP_1", fk_2 + r1)
    return (a)

S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

k=list(map(int, input("\nEnter 10 bits (key): ").strip().split()))[:10] #1 0 1 0 0 0 0 0 1 0
k1,k2=key_generation(k)
plain_text = list(map(int, input("\nEnter  8 bits (plain text): ").strip().split()))[:8]# 1 0 0 1 0 1 1 1
a = Sdes(k1,k2, plain_text)
b = Sdes(k2,k1, a)#0,0,1,1,1,1,1,1
print("\nEncrypted:           " + str(a))
print("\nDecrypted:           " + str(b))