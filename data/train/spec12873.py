import numpy as np 

def function(x):

	w9 = 2
	n8 = 3
	paths = []
	try:
		if w9 > 8:
			x = x+3
			paths.append(1)
		else:
			x = x/w9
			paths.append(2)
		if x > 7:
			x = x/x
			w9 = x+9
			paths.append(3)
		else:
			w9 = 1+w9
			w9 = w9*n8
			w9 = w9*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))