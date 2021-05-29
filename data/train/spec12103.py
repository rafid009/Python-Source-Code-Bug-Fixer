import numpy as np 

def function(x):

	x1 = x
	o9 = 5
	paths = []
	try:
		if x >= 1:
			x1 = x1/2
			o9 = o9/x
			x1 = x1/x1
			paths.append(1)
		else:
			x = x1+x1
			paths.append(2)
		if o9 >= 1:
			x = x*7
			paths.append(3)
		else:
			x1 = o9+3
			x = x*3
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x = x1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))