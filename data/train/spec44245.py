import numpy as np 

def function(x):

	n0 = 9
	e3 = x
	paths = []
	try:
		if n0 <= 6:
			n0 = n0-8
			paths.append(1)
		else:
			n0 = 2/n0
			paths.append(2)
		if x <= 2:
			x = x-x
			n0 = 2+7
			x = 3/4
			paths.append(3)
		else:
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))