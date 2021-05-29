import numpy as np 

def function(x):

	e4 = x
	d8 = x
	paths = []
	try:
		if d8 >= 6:
			e4 = x*x
			x = x/e4
			paths.append(1)
		else:
			x = x-6
			e4 = 3/2
			paths.append(2)
		if d8 < 3:
			x = 0/x
			e4 = d8+e4
			x = 7+x
			paths.append(3)
		else:
			e4 = 0-2
			x = x/9
			e4 = 6/e4
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		x = d8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))