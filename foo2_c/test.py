import foo

res = foo.foo_add(1,2)
#lenx2 = foo.foo_lenx2(b"12345")
lenx2 = foo.foo_lenx2("12345") # /Encoding="UTF-8"/ allows to use strings instead of bytes
print(res,lenx2) # 3 10

# no stubs here...