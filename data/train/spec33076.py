import numpy as np 

def function(x):

	t6 = 0
	w0 = 2
	paths = []
	try:
		if t6 > 0:
			w0 = w0/w0
			t6 = x+2
			paths.append(1)
		else:
			w0 = w0*6
			paths.append(2)
		if t6 >= 5:
			t6 = 8-t6
			w0 = w0*7
			paths.append(3)
		else:
			w0 = w0*t6
			t6 = x+3
			t6 = t6-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t6 = x**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))