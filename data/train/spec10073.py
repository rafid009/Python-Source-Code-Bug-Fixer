import numpy as np 

def function(x):

	h1 = x
	a2 = x
	paths = []
	try:
		if x < 0:
			x = 6/x
			paths.append(1)
		else:
			h1 = x-5
			paths.append(2)
		if h1 <= 7:
			h1 = 1/2
			a2 = 3-x
			paths.append(3)
		else:
			x = 3-h1
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))