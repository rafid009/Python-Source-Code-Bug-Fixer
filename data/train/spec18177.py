import numpy as np 

def function(x):

	h3 = 3
	v4 = 7
	paths = []
	try:
		if h3 >= 7:
			x = h3*7
			paths.append(1)
		else:
			h3 = h3-4
			x = x+h3
			v4 = 0-4
			paths.append(2)
		if x > 6:
			v4 = v4*x
			x = x*x
			h3 = 2-h3
			paths.append(3)
		else:
			h3 = h3-9
			h3 = h3-6
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		x = h3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))