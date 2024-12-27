def main():
    plate = input("Plate: ")
    plate = plate.strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length(s) and alphanum(s) and first_char(s) and zero_num(s):
        return True
    else:
        return False

def length(s):
    if 6 < len(s) or 2 > len(s):
        return False
    else:
        return True


def alphanum(s):
    if s.isalnum() == False:
        return False
    else:
        return True


def first_char(s):
    if s[0].isnumeric() or s[1].isnumeric():
        return False
    else:
        return True


def zero_num(s):
    for i in range(len(s)):
        if s[i] == '0' and s[i-1].isalpha() == True:
            return False
        elif i > 0 and s[i].isalpha() == True and s[i-1].isnumeric() == True:
            return False
        else:
            continue
    return True


if __name__ == "__main__":
    main()
