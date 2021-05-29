import numpy as np 

def function(x):

	e8 = 5
	h2 = 7
	paths = []
	try:
		if h2 <= 7:
			e8 = 5+e8
			e8 = x+e8
			x = x*5
			paths.append(1)
		else:
			x = h2/x
			paths.append(2)
		if x <= 6:
			h2 = h2+h2
			e8 = e8+5
			e8 = e8/x
			paths.append(3)
		else:
			h2 = h2+4
			e8 = 0+e8
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