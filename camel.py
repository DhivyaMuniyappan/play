def camel(word):
    return ''.join(x.capitalize() or ' ' for x in word.split(' '))

print(camel('may  god  bless  you'))
