f = open("text.txt", "r")
text = f.read()

text = text.replace("\n", "").lower()

for i in text:
    if ord(i) in range(20, 65):
        text = text.replace(str(i), "")

l_text = len(text)
let = 97
percent = {}
for letter in range(0, 26):  # 97-122
    count = 0
    for i in text:
        if ord(i) == let:
            count += 1
    percent.update({str(chr(let)): round(count / l_text * 100, 4)})
    let += 1
sort_percent = sorted(percent.items(), key=lambda x: x[1],reverse=True)

for key, value in sort_percent:
    print(key, ":", value)
