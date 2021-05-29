import numpy as np 

def function(x):

	h1 = x
	n5 = 0
	x = 9
	paths = []
	try:
		if h1 < 4:
			x = x-x
			x = x-h1
			h1 = x*7
			paths.append(1)
		else:
			h1 = x-x
			paths.append(2)
		if n5 > 5:
			x = 4/7
			paths.append(3)
		else:
			x = n5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))