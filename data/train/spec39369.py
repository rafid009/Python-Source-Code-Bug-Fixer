import numpy as np 

def function(x):

	a8 = x
	h3 = 1
	paths = []
	try:
		if x >= 9:
			a8 = 3-a8
			paths.append(1)
		else:
			a8 = 5/7
			paths.append(2)
		if a8 < 6:
			x = 6*x
			a8 = a8+4
			h3 = 9-h3
			paths.append(3)
		else:
			h3 = h3+h3
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		a8 = a8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))