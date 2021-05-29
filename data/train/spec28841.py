import numpy as np 

def function(x):

	v9 = 6
	d3 = 1
	paths = []
	try:
		if x > 9:
			x = x-1
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if x <= 1:
			x = v9*6
			v9 = x*6
			x = x/v9
			paths.append(3)
		else:
			x = 4+x
			v9 = x-4
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d3 = x**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))