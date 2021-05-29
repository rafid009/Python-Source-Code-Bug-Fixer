import numpy as np 

def function(x):

	y5 = 4
	e2 = 2
	paths = []
	try:
		if x > 9:
			y5 = 2/y5
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if x > 7:
			e2 = 9/8
			e2 = 0-e2
			y5 = 3-y5
			paths.append(3)
		else:
			e2 = 2-9
			e2 = 5-y5
			e2 = x+9
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		e2 = y5**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))