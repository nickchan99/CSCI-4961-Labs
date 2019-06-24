cmake_minimum_required(VERSION 3.3)
project(static_block)

add_library(BlockLib source/block.c)

list(APPEND EXTRA_LIBS BlockLib)
list(APPEND EXTRA_INCLUDES headers/block.h)

add_executable(static_block program.c)

target_link_libraries(static_block ${EXTRA_LIBS})
