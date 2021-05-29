import numpy as np 

def function(x):

	e8 = 3
	b0 = x
	paths = []
	try:
		if x < 5:
			x = x-e8
			x = e8*x
			paths.append(1)
		else:
			e8 = e8/x
			paths.append(2)
		if e8 >= 5:
			e8 = e8-b0
			x = b0*5
			b0 = e8-x
			paths.append(3)
		else:
			x = x+e8
			e8 = x+2
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		e8 = b0**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))