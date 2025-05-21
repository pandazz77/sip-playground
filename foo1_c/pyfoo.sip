%Module(name=foo, language="C")

%ModuleCode
#include <foo.h>
%End

int foo_add(int a, int b);
int foo_lenx2(char *str /Encoding="UTF-8"/);