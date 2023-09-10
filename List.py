import operator

friends = ["Kevin", "Kevin", "Jim", "Ture", "Laban", "Roger"]
friends2 = ["Kev", "kev", "kluro", "styre", "Lajban", "Rune"]

a = []
sa = []
b = []
c = friends2
c.clear()

print(c)
print(friends2)
for i in friends:
    a.append(i)
sa.append("\n".join(map(str, a)))
print(sa[-1])
print()

print(friends2[1:3])
friends.extend(("a", "b"))
print(friends[0])
if friends[0] == "Kevin":
    print("JA")
else:
    print("NEJ")



e_remove =("Kevin", "Kevin", "Jim")
f_list = []
for element in friends:
    if element not in e_remove:
        f_list.append(element)

print(f_list)
b.append(" ".join(friends))
print(b)
print(c)
if b[0] == str("Kevin"):
    print("JA")
else:
    print("NEJ")

print("\u2764\ufe0f")




