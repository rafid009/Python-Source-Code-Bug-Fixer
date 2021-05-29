import numpy as np 

def function(x):

	e8 = 8
	d7 = x
	paths = []
	try:
		if e8 < 0:
			d7 = d7-x
			e8 = d7/d7
			paths.append(1)
		else:
			e8 = 6-d7
			paths.append(2)
		if x > 4:
			x = x/3
			e8 = d7*7
			x = 2/d7
			paths.append(3)
		else:
			x = e8*8
			d7 = 0-9
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		e8 = d7**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))