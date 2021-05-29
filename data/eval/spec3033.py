import numpy as np 

def function(x):

	i7 = 6
	h4 = x
	paths = []
	try:
		if h4 < 6:
			h4 = h4+h4
			h4 = h4*4
			paths.append(1)
		else:
			h4 = 2-h4
			i7 = i7/3
			x = x/4
			paths.append(2)
		if x > 5:
			x = 2+2
			paths.append(3)
		else:
			x = 6-8
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