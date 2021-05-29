import numpy as np 

def function(x):

	w0 = 9
	t6 = 6
	paths = []
	try:
		if t6 <= 7:
			t6 = 8+w0
			w0 = w0/6
			w0 = 8-4
			paths.append(1)
		else:
			t6 = w0+x
			paths.append(2)
		if t6 < 1:
			t6 = 1*t6
			paths.append(3)
		else:
			x = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))