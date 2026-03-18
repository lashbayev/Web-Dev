#1
def sleep_in(weekday, vacation):
    return not weekday or vacation

#2
def diff21(n):
    if n > 21:
        return (n - 21) * 2
    return 21 - n

#3
def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

#4
def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10

#5
def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

#6
def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10
```

#7
def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    return (a < 0) != (b < 0)

#8
def not_string(str):
    if str.startswith('not'):
        return str
    return 'not ' + str

#9
def missing_char(str, n):
    return str[:n] + str[n+1:]
