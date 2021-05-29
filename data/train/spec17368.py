import numpy as np 

def function(x):

	a9 = 8
	h4 = 8
	paths = []
	try:
		if a9 < 1:
			x = x/x
			h4 = 4*h4
			paths.append(1)
		else:
			h4 = 2*h4
			paths.append(2)
		if h4 >= 7:
			a9 = a9-x
			paths.append(3)
		else:
			h4 = 9-h4
			a9 = a9/3
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		a9 = a9**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))