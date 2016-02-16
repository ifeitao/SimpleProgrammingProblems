def is_palindrome(text):
    result = True
    for i in range(0, len(text) // 2):
        if text[i] != text[-i - 1]:
            result = False
            break
    return result

if __name__ == "__main__":
    input_str = input("Please input a string:\n")
    if is_palindrome(input_str):
        print("%s is a palindrome" % input_str)
    else:
        print("%s is not a palindrome" % input_str)
