project(foo LANGUAGES C)

add_library(${PROJECT_NAME} foo.h foo.c)
add_executable(${PROJECT_NAME}_bin foo.h foo.c main.c)