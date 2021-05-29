import numpy as np 

def function(x):

	e4 = 4
	d9 = 3
	paths = []
	try:
		if x > 9:
			d9 = 5-d9
			e4 = 4*e4
			paths.append(1)
		else:
			d9 = e4+e4
			e4 = e4-x
			e4 = 8*8
			paths.append(2)
		if d9 <= 4:
			e4 = e4-1
			paths.append(3)
		else:
			e4 = 6-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))