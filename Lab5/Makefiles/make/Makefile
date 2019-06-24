static_block: program.c libblockstatic.a
	gcc -Wall program.c -o static_block -L. -lblockstatic
dynamic_block: program.c libblockshared.so
	gcc -L. -Wl,-rpath=. -Wall program.c -o dynamic_block -lblockshared
libblockstatic.a: block.o headers/block.h
	ar rcs libblockstatic.a block.o headers/block.h
libblockshared.so: block.o headers/block.h
	gcc -shared block.o -o libblockshared.so 
block.o: source/block.c
	gcc -fPIC -c source/block.c -o block.o
libs: libblockstatic.a
clean:
	rm -f static_block dynamic_block *.o *.so *.a