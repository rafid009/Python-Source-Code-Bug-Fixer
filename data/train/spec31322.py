import numpy as np 

def function(x):

	a3 = x
	h1 = x
	x = 1
	paths = []
	try:
		if x <= 9:
			x = 8-x
			h1 = h1/6
			h1 = 7/x
			paths.append(1)
		else:
			x = a3+3
			a3 = 8+a3
			paths.append(2)
		if a3 < 3:
			x = 5-x
			paths.append(3)
		else:
			h1 = h1+a3
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))