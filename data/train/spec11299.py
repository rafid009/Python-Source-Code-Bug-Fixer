import numpy as np 

def function(x):

	e9 = 1
	h2 = x
	paths = []
	try:
		if e9 <= 4:
			h2 = 7/x
			paths.append(1)
		else:
			e9 = e9+h2
			h2 = h2*6
			paths.append(2)
		if x > 0:
			x = 3+6
			h2 = h2+0
			paths.append(3)
		else:
			e9 = e9/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))