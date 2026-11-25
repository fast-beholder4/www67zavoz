text = ' Hello, Python! '

one = text.strip()
print(one)

two = one.replace('!', '?')
print(two)

three = two.upper()
print(three)

result = text.strip().lower()
print(result)

assert result == 'hello, python!'