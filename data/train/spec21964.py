import numpy as np 

def function(x):

	w8 = x
	m4 = 3
	paths = []
	try:
		if m4 > 1:
			x = x-9
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if w8 >= 3:
			w8 = w8+4
			paths.append(3)
		else:
			x = 2+x
			x = 9+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w8 = x**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))