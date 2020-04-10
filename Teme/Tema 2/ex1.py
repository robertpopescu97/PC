string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
a = (string[4:14])
b = (string[25:31])
c = (string[42:49])
new_string = string.replace(a, "Conquistador").replace(b, "King").replace(c, "Palace")
print(new_string)