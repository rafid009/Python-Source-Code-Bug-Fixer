import numpy as np 

def function(x):

	v9 = x
	d3 = 5
	paths = []
	try:
		if v9 > 8:
			x = x*3
			x = x+x
			v9 = 1+2
			paths.append(1)
		else:
			x = x-x
			x = 3/7
			x = v9*3
			paths.append(2)
		if v9 > 0:
			x = 2/1
			paths.append(3)
		else:
			v9 = v9/d3
			v9 = 2*d3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))