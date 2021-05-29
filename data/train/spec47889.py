import numpy as np 

def function(x):

	h6 = x
	x3 = x
	paths = []
	try:
		if x3 > 5:
			h6 = h6+x
			paths.append(1)
		else:
			h6 = h6-0
			paths.append(2)
		if x3 > 7:
			x3 = x3-0
			paths.append(3)
		else:
			x3 = x-0
			x3 = x/x3
			x3 = 2*h6
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		x3 = h6**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))