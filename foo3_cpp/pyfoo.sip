%Module(name=pyfoo, language="C++")
%DefaultEncoding "UTF-8"

class Foo {
    %TypeHeaderCode
    #include <foo.h>
    %End

    public:
        Foo(int, const char*);

        void set_int_val(int);
        int get_int_val();

        void set_string_val(const char*);
        char* get_string_val();
};