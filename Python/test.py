def is_love_letter_reproducible(L = "I love you ", M = "abcdefghijklmnopqrstuvwxyz"):
    char_code = ""
    char_count = 0

    while char_count < len(L):
        char_code = L[char_count].lower()
        for i in M:
            if char_code == i.lower():
                print(char_count, char_code, i)
                char_count +=1
                break
        if char_code != i:
            if char_code != " ":
                print("gago")
                return False
            else:
                char_count +=1
    
    print("Hello World!")

    
    
is_love_letter_reproducible()