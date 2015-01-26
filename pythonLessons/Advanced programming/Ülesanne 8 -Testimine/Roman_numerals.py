"""
Pretty crappy and buggy Roman numeral converter

@author Cody McPhail 
"""

def convert(input):
    """
    A smaller number in front of a larger number means subtraction, all else means addition.
    For example, IV means 4, VI means 6.

    You would not put more than one smaller number in front of a larger number to subtract.
    For example, IIV would not mean 3.

    You must separate ones, tens, hundreds, and thousands as separate items.
    That means that 99 is XCIX, 90 + 9, but never should be written as IC. 
    Similarly, 999 cannot be IM and 1999 cannot be MIM.
    """
    if type(input) == str:
        if len(input.replace("M", "").replace("D", "").replace("C", "").replace("L", "").replace("X", "").replace("V", "").replace("I", "")) != 0:
            return -1
        sum = 0
        if input.find("IIIII") != -1 or input.find("VV") != -1 or input.find("XXXXX") != -1 or \
        input.find("DD") != -1 or input.find("CCCCC") != -1:
            return -1
        if input.find("IIV") != -1 or input.find("IIX") != -1 or input.find("IL") != -1 or \
        input.find("IC") != -1 or input.find("ID") != -1 or input.find("IM") != -1 \
        or check_separation(input):
            return - 1
        for i, char in enumerate(input):
            if char == 'M':
                if larger_number_after(i, char, input):
                    sum = sum - 1000
                else:
                    sum = sum + 1000
            elif char == 'D':
                if larger_number_after(i, char, input):
                    sum = sum - 500
                else:
                    sum = sum + 500
            elif char == 'C':
                if larger_number_after(i, char, input):
                    sum = sum - 100     # bug here, was: sum -= sum - 100
                else:
                    sum = sum + 100
            elif char == 'L':
                if larger_number_after(i, char, input):
                    sum = sum - 50
                else:
                    sum = sum + 50
            elif char == 'X':
                if larger_number_after(i, char, input):
                    sum = sum - 10
                else:
                    sum = sum + 10
            elif char == 'V':
                if larger_number_after(i, char, input):
                    sum = sum - 5
                else:
                    sum = sum + 5
            elif char == 'I':
                if larger_number_after(i, char, input):
                    sum = sum - 1
                else:
                    sum = sum + 1
        return sum
    else:
        return -1 # added else
    
def check_separation(string):
    numerals = [("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)]
    idx = {'I': 0, 'V': 1, 'X': 2, 'L': 3, 'C': 4, 'D': 5, 'M': 6}
    for i, char in enumerate(string):
        if i < len(string)-1:
            if string[i+1] == char and larger_number_after(i+1, char, string):
                return True
            for j in range(idx[char]+1, len(numerals)):
                if i < len(string)-1 and char != 'I':
                    if string[i+1] == "M" and string[i] == "C" or \
                    string[i+1] == "X" and string[i] == "C" or \
                    string[i+1] == "C" and string[i] == "X" or \
                    string[i+1] == "D" and string[i] == "C" or \
                    string[i+1] == "L" and string[i] == "X":
                        pass
                    elif string[i+1] == numerals[j][0]:
                        return True
                pass
    return False

def larger_number_after(i, char, string):
    numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in range(i, len(string)-1):
        if numerals[string[i+1]] > numerals[char]:
            return True
    return False
     

def main():
    print(convert("VII"))
    print(convert("IX"))
    print(convert("XX"))
    
if __name__ == "__main__":
    main()
