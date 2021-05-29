import numpy as np 

def function(x):

	h6 = 2
	v3 = x
	paths = []
	try:
		if x > 2:
			x = 5-x
			paths.append(1)
		else:
			x = v3-h6
			v3 = 6/5
			h6 = h6/h6
			paths.append(2)
		if v3 >= 4:
			h6 = 9-6
			x = 1-x
			x = x*8
			paths.append(3)
		else:
			x = v3*x
			x = x+5
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