import numpy as np 

def function(x):

	k4 = x
	h1 = 5
	paths = []
	try:
		if x >= 6:
			k4 = 1-9
			k4 = 1-k4
			x = x/1
			paths.append(1)
		else:
			h1 = h1-9
			h1 = x+x
			paths.append(2)
		if k4 >= 0:
			h1 = 5-h1
			x = x+0
			paths.append(3)
		else:
			x = h1+7
			x = x+k4
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