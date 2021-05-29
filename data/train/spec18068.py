import numpy as np 

def function(x):

	e5 = 3
	h6 = 7
	paths = []
	try:
		if x < 9:
			e5 = e5+7
			paths.append(1)
		else:
			x = 0*2
			paths.append(2)
		if e5 >= 0:
			x = 0-x
			h6 = h6+h6
			e5 = 5*h6
			paths.append(3)
		else:
			e5 = 0/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))