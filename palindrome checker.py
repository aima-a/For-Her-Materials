def check_palindrome(input_string):
    def is_palindrome(s):
        s = s.strip().replace(" ", "").lower()
        return s == s[::-1]

    if is_palindrome(input_string):
        return "The sequence is a palindrome"
    else:
        return "The sequence is not a palindrome"

input_string = input("Enter the string: ")
result = check_palindrome(input_string)
print(result)
