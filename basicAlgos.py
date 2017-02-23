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

print (reverse_string("asdf"))