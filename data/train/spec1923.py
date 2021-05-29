import numpy as np 

def function(x):

	w9 = x
	d2 = x
	paths = []
	try:
		if d2 >= 6:
			w9 = w9+2
			w9 = 4/w9
			x = 0-8
			paths.append(1)
		else:
			d2 = 0*d2
			d2 = w9+d2
			paths.append(2)
		if w9 <= 4:
			d2 = 9+d2
			x = 7*9
			w9 = 5/1
			paths.append(3)
		else:
			w9 = 1/w9
			w9 = 3+x
			x = 1-x
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