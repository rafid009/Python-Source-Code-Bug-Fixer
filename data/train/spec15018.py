import numpy as np 

def function(x):

	x1 = 8
	w6 = 4
	paths = []
	try:
		if x < 4:
			x1 = x1*3
			x1 = x1-9
			paths.append(1)
		else:
			x = x*x1
			w6 = w6+x1
			w6 = x-x
			paths.append(2)
		if x1 < 8:
			x1 = x1-9
			x1 = x1-9
			paths.append(3)
		else:
			w6 = 0*w6
			x1 = w6/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x1 = x**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))