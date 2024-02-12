if __name__ == "__main__":
    entry = input().split(" ")
    str_number = entry[0]
    repetition = int(entry[1])
    number = int(str_number)
    counter = 0
    while counter < repetition:
        if int(str_number[-1]) == 0:
            number = int(number/10)
            counter+=1
            str_number = str(number)
        else:
            number = int(number - 1)
            counter+=1
            str_number = str(number)

    print(number)
    