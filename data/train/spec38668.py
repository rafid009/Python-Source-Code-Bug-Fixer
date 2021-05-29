import numpy as np 

def function(x):

	h6 = x
	l8 = 0
	x = x
	paths = []
	try:
		if h6 >= 1:
			h6 = x/x
			paths.append(1)
		else:
			x = 3-x
			x = 0*x
			x = 6+0
			paths.append(2)
		if x <= 6:
			h6 = h6+5
			paths.append(3)
		else:
			h6 = l8*h6
			h6 = 2+h6
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		l8 = h6**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))