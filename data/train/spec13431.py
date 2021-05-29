import numpy as np 

def function(x):

	l8 = 2
	h1 = 5
	paths = []
	try:
		if h1 < 1:
			h1 = h1-h1
			paths.append(1)
		else:
			x = x+h1
			l8 = l8+9
			paths.append(2)
		if l8 >= 8:
			x = 6-x
			x = x-9
			paths.append(3)
		else:
			x = l8/3
			x = x*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))