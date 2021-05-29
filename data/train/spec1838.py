import numpy as np 

def function(x):

	y5 = x
	h4 = 7
	paths = []
	try:
		if y5 >= 2:
			y5 = 9-y5
			x = y5+x
			paths.append(1)
		else:
			h4 = x*h4
			paths.append(2)
		if y5 >= 1:
			y5 = 5-y5
			h4 = h4/8
			y5 = y5-h4
			paths.append(3)
		else:
			x = x+1
			h4 = 4*h4
			x = x+x
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		x = y5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))