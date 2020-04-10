string = " The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
a = (string[5:15])
b = (string[26:32])
c = (string[43:50])
new_string = string.replace(a, "Conquistador").replace(b, "King").replace(c, "Palace")
print(new_string)