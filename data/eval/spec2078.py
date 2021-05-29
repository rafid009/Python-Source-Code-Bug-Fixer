import numpy as np 

def function(x):

	y5 = x
	h4 = x
	paths = []
	try:
		if y5 < 4:
			x = x+5
			x = x+4
			y5 = y5*x
			paths.append(1)
		else:
			h4 = h4+1
			h4 = y5*h4
			h4 = x/7
			paths.append(2)
		if y5 > 3:
			h4 = h4-y5
			paths.append(3)
		else:
			x = 0*x
			x = 1-x
			x = x*x
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