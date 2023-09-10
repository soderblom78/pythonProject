lucky_numbers = [4, 8, 15, 16, 23, 42, 42]
friends = ["Kevin", "Karen", "Jim, Ture", "Laban", "Roger", "Laban"]
friends.extend(lucky_numbers)
friends.append(" Elvis")
friends.insert(1, " Kelly")
print(friends)
print(friends.index("Kevin"))
friends.remove("Kevin")
print(friends)
friends.isupper()
