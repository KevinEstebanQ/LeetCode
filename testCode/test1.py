def print_word(s:str):
    with open("logs.txt", "w") as f:
        for i in range(len(s)):
            for j in range(0, i+1):
                print(s[j], file=f, end="")
            print("", file=f)

print_word(s="kevin")