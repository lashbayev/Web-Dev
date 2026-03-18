#1
def hello_name(name):
    return f'Hello {name}!'

#2
def make_abba(a, b):
    return a + b + b + a


#3
def first_half(str):
    return str[:len(str)//2]

#4
def without_end(str):
    return str[1:-1]

#5
def combo_string(a, b):
    if len(a) < len(b):
        return a + b + a
    return b + a + b
```

#6
def non_start(a, b):
    return a[1:] + b[1:]

#7
def left2(str):
    return str[2:] + str[:2]

#8
def left2(str):
    return str[2:] + str[:2]
