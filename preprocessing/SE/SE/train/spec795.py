import numpy as np 

def function(x):

	d6 = 6
	j9 = x
	x = x
	paths = []
	try:
		if j9 > 7:
			d6 = j9/d6
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if x < 1:
			x = 5*x
			paths.append(3)
		else:
			d6 = 4/8
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