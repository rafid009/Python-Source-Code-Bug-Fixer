import numpy as np 

def function(x):

	w9 = x
	v2 = 9
	paths = []
	try:
		if w9 > 6:
			v2 = 3*v2
			paths.append(1)
		else:
			x = x+5
			w9 = v2/4
			paths.append(2)
		if w9 < 4:
			v2 = 3*v2
			v2 = 5*3
			paths.append(3)
		else:
			x = 1-x
			w9 = 7-w9
			w9 = w9-v2
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