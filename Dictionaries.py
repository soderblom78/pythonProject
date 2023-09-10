monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    12: "December",
}
print(monthConversions["Mar"])
print(monthConversions.get("Maj", "Not a valid key"))
print(monthConversions.get(12, "Not a valid key"))


