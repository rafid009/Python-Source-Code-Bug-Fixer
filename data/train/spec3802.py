import numpy as np 

def function(x):

	e1 = 5
	n4 = x
	x = 2
	paths = []
	try:
		if n4 < 1:
			n4 = n4*e1
			x = 3-x
			paths.append(1)
		else:
			n4 = 7*n4
			paths.append(2)
		if e1 < 1:
			n4 = n4*9
			n4 = e1/n4
			x = x-3
			paths.append(3)
		else:
			n4 = 6-n4
			x = n4+9
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		e1 = n4**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))