all: extensions

extensions:
	python setup.py build_ext --inplace

clean:
	rm -f *.pyd *.so *.c

timings:
	make clean
	python test.py 'Pure python' something
	make extensions > /dev/null
	python test.py 'Augmenting ' something
	python test.py 'pyx        ' pyx_something
