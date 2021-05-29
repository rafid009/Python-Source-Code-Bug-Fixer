import numpy as np 

def function(x):

	x3 = 6
	d6 = 3
	paths = []
	try:
		if x3 > 1:
			x = x/8
			x3 = x3/1
			paths.append(1)
		else:
			x = 4-x3
			d6 = d6*x
			paths.append(2)
		if x3 >= 2:
			d6 = 3/2
			d6 = d6+3
			d6 = 5-d6
			paths.append(3)
		else:
			d6 = d6+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))