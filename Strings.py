phrase = "Giraffe Academy"
print(phrase)
print(phrase.replace("Academy", "Snopp"))
print (phrase.lower())
print (phrase.index("i"))
print (phrase[3])
print(len(phrase))

a = []

x = range(5)
for i in x:
    i = input()
    if len(i) == 0:
        break
    else:
        a.append(i)


print("\n".join(map(str, a)))



















