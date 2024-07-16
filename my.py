x = 2    # int
y = 2.8  # float
z = 1j   # complex
# if elif else statement 
if x < 2:
    print('ok')
elif x == 2:
    print('not ok')
else:
    print('yes')
# data type 
print(type(x))
print(type(y))
print(type(z))

# slicing word 
b = "Hello, World!"
print(b[:10])
# modify your string 
a = "Hello, World!. new"
print(a.upper())
print(a.lower())
print(a.replace('H','G'))

# concatation 
a = "Hello"
b = "World"
c = a + b
d = a + " " + b
print(c)
print(d)

age = 36
txt = f"My name is John, I am {age}" #if not using f it will not working
print(txt)

#for  any words
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# for line spacing 
txt = "Hello\rWorld\rBack!"
print(txt) 

#shuru theke koto number a ache ta janar jonne akhane o theke count shuru hoi
txt = "Hello, welcome to my world."
x = txt.index("elcome")
y = txt.count("e")
print(x)
#for count total word , letter etc
print(y)

# for join 
myTuple = ("John", "Peter", "Vicky")
x = " ".join(myTuple)
y = "+".join(myTuple)
z = "z".join(myTuple)
print(x)
print(y)
print(z)




