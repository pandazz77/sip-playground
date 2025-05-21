%Module(name=foo, language="C")
%DefaultEncoding "UTF-8"

%ModuleCode
#include <foo.h>
%End

int foo_add(int a, int b);
int foo_lenx2(char *str);