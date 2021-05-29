import numpy as np 

def function(x):

	e8 = x
	h9 = 7
	paths = []
	try:
		if e8 >= 8:
			x = x+x
			e8 = h9+e8
			paths.append(1)
		else:
			e8 = e8-0
			e8 = 7*e8
			e8 = 5/e8
			paths.append(2)
		if h9 <= 9:
			h9 = 2/x
			x = 1*x
			paths.append(3)
		else:
			e8 = h9*e8
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		e8 = h9**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))