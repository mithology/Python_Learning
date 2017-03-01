def add(a,b):
    return a+b;
print(add(4,3));

def reverse_string(word):
    reversed_word =""
    size =len(word)
    while size:
        size -=1
        reversed_word +=word[size]
    return reversed_word
print (reverse_string("asd sxcxk  djicj djcidj f"))

def factorial_for_whole_number(number):
    product =1;
    for i in range(2,number+1):
        product = product*i;
    return product

print(factorial_for_whole_number(19))