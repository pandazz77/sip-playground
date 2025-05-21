project(foo LANGUAGES CXX)

add_library(${PROJECT_NAME} foo.h foo.cpp)
add_executable(${PROJECT_NAME}_bin foo.h foo.cpp main.cpp)

set_property( # for cpp sip project (-fPic)
    TARGET ${PROJECT_NAME}
    PROPERTY POSITION_INDEPENDENT_CODE
    ON
)