import numpy as np 

def function(x):

	d8 = 9
	e9 = x
	paths = []
	try:
		if x <= 5:
			x = x/e9
			e9 = e9/6
			e9 = 2/9
			paths.append(1)
		else:
			x = 0-x
			x = x+d8
			d8 = d8/x
			paths.append(2)
		if x >= 8:
			x = x-2
			paths.append(3)
		else:
			d8 = 9*d8
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		e9 = d8**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))