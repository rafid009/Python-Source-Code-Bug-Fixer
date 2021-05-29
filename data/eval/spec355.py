import numpy as np 

def function(x):

	e8 = 6
	h3 = 4
	paths = []
	try:
		if h3 >= 9:
			h3 = e8/9
			x = x*e8
			paths.append(1)
		else:
			h3 = h3/8
			e8 = e8*8
			paths.append(2)
		if e8 <= 1:
			x = 4*h3
			h3 = h3/7
			x = x*4
			paths.append(3)
		else:
			e8 = 5-e8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))