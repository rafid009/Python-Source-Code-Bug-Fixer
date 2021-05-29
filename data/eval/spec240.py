import numpy as np 

def function(x):

	h6 = 2
	f9 = 7
	paths = []
	try:
		if h6 > 5:
			x = x+h6
			f9 = 5/3
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if f9 > 1:
			h6 = h6/h6
			paths.append(3)
		else:
			h6 = x-8
			f9 = 0/f9
			f9 = f9*5
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