all: extensions

extensions:
	python setup.py build_ext --inplace

clean:
	rm -f *.pyd *.so *.c *.pyc
	rm -rf build/

timings:
	echo 'Module-type result time' > output
	make clean
	python test.py 'Pure python' something >> output
	make extensions > /dev/null
	python test.py 'Augmenting ' something >> output
	python test.py 'pyx        ' pyx_something >> output
	cat output
	rm output
