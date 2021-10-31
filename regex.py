import re

string = "i want to play basketball"

x = re.search("(?<=i want to play).*$", string)
print(x.group().strip())