import numpy as np 

def function(x):

	e5 = 2
	n4 = 1
	paths = []
	try:
		if x <= 3:
			x = x/e5
			x = 6-x
			paths.append(1)
		else:
			x = x/6
			n4 = 5/8
			n4 = 5-n4
			paths.append(2)
		if e5 <= 2:
			x = x-4
			paths.append(3)
		else:
			n4 = n4*x
			e5 = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))