#include <stdio.h>

#include "foo.h"

int main(int argc, char *argv[]){
    int res = foo_add(2,3);

    printf("%d\n",res);

    return 0;
};