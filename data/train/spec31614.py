import numpy as np 

def function(x):

	e0 = x
	y2 = x
	paths = []
	try:
		if x < 9:
			x = x/x
			e0 = 6+e0
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if e0 >= 2:
			e0 = e0/3
			e0 = x+6
			paths.append(3)
		else:
			x = x+e0
			e0 = x*e0
			x = 0/6
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		y2 = y2**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))