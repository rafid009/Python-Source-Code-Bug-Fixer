import numpy as np 

def function(x):

	w6 = 4
	n1 = 2
	x = 7
	paths = []
	try:
		if w6 <= 6:
			x = 0*x
			x = x-6
			paths.append(1)
		else:
			n1 = x*n1
			x = 0/x
			paths.append(2)
		if w6 >= 6:
			n1 = 1+3
			x = w6/w6
			paths.append(3)
		else:
			w6 = n1+x
			x = x-w6
			n1 = n1/6
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