import numpy as np 

def function(x):

	j9 = 3
	h6 = x
	paths = []
	try:
		if j9 >= 0:
			x = x+h6
			paths.append(1)
		else:
			x = 9*x
			paths.append(2)
		if x > 7:
			x = 7/x
			paths.append(3)
		else:
			h6 = x-j9
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		x = h6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))