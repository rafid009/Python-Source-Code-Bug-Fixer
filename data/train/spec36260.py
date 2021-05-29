import numpy as np 

def function(x):

	u5 = x
	h4 = x
	paths = []
	try:
		if h4 > 1:
			h4 = 1+x
			paths.append(1)
		else:
			h4 = 4/h4
			h4 = h4*x
			paths.append(2)
		if h4 < 1:
			h4 = u5-u5
			paths.append(3)
		else:
			x = x+9
			u5 = 1*u5
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