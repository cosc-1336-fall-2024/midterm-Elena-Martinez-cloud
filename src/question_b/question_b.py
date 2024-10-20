#write functions here, don't add input('') statements here!
def test_config():
    return True

def reverse_string(string1):
    reverse_string = ""
    index = len(string1)-1
    while index >= 0:
        reverse_string += string1[index]
        index -= 1

    return reverse_string

print (reverse_string("test"))

#print(test_config())