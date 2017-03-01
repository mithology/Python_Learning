def add(a, b):
    return a + b;


def reverse_string(word):
    reversed_word = ""
    size = len(word)
    while size:
        size -= 1
        reversed_word += word[size]
    return reversed_word


def factorial_for_whole_number(number):
    product = 1
    for i in range(1, number + 1):
        product = product * i
    return product


def is_palindrome(word):
    size = len(word)
    palindrome = True
    for i in range(0, size - 1):
        if (word[i] != word[size - 1 - i]):
            palindrome = False
    return palindrome


print(add(4, 3))
print (reverse_string("asd sxcxk  djicj djcidj f"))
print(factorial_for_whole_number(19))
print (is_palindrome("sarma"))
print (is_palindrome("MAAM"))
