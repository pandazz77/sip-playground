from pyfoo import Foo

x = Foo(5,"hello")

print(x.get_int_val())
print(x.get_string_val())

x.set_int_val(50)
x.set_string_val("world")

print(x.get_int_val())
print(x.get_string_val())