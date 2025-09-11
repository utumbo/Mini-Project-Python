with open("PinPass.txt", "w") as writeToPinPass:
    for i in range(100, 1000):
        writeToPinPass.write(f"{i}\n")