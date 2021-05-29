import numpy as np 

def function(x):

	t2 = 6
	w0 = x
	paths = []
	try:
		if x > 0:
			t2 = w0+t2
			w0 = t2-x
			paths.append(1)
		else:
			t2 = 7*6
			paths.append(2)
		if w0 >= 6:
			x = x*t2
			x = 1/x
			paths.append(3)
		else:
			t2 = 9+2
			t2 = 8+t2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))