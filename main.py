import colored,random

message = input("yazı lütfen")

randomcolor = random.choice(colored.names).lower()

for i in message:
    print(colored.fg(randomcolor),end="")
    print(colored.attr("reset",end="")
    randomcolor = random.choice(colored.names).lower()
