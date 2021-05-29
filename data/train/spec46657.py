import numpy as np 

def function(x):

	x0 = x
	w9 = 0
	paths = []
	try:
		if w9 <= 4:
			w9 = w9-w9
			x = x+x
			x0 = x0*x0
			paths.append(1)
		else:
			x = x*1
			paths.append(2)
		if x > 6:
			x = 3-x
			x = 0+x
			paths.append(3)
		else:
			w9 = x0/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))