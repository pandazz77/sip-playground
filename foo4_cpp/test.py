from pyfoo import Foo

help(Foo)

x = Foo(5,"hello")
x.int_val

print(x.int_val)
print(x.string_val)

x.int_val = 50
x.string_val = "world"

print(x.int_val)
print(x.string_val)