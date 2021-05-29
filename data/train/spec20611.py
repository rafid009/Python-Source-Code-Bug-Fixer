import numpy as np 

def function(x):

	n1 = 1
	w5 = x
	x = 2
	paths = []
	try:
		if n1 > 2:
			w5 = 1-w5
			x = 3+x
			paths.append(1)
		else:
			n1 = n1/7
			w5 = 3*w5
			x = x/4
			paths.append(2)
		if n1 < 7:
			x = x-1
			paths.append(3)
		else:
			w5 = 5*w5
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