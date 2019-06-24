cmake_minimum_required(VERSION 3.3)
project(CMakeExample)

set(CMAKE_CXX_STANDARD 14)

add_library(blocklibstat STATIC source/block.c headers/block.h)
add_library(blocklibshar SHARED source/block.c headers/block.h)

list(APPEND STATIC_LIBS blocklibstat)
list(APPEND DYNAMIC_LIBS blocklibshar)

add_executable(static_block program.c)
add_executable(dynamic_block program.c)

target_link_libraries(static_block ${STATIC_LIBS})
target_link_libraries(dynamic_block ${DYNAMIC_LIBS})

