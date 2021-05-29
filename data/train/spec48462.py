import numpy as np 

def function(x):

	a9 = 0
	d6 = 6
	paths = []
	try:
		if d6 > 3:
			a9 = a9+2
			a9 = 4-1
			paths.append(1)
		else:
			d6 = 0+d6
			paths.append(2)
		if x <= 5:
			x = 3-x
			paths.append(3)
		else:
			d6 = d6*4
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