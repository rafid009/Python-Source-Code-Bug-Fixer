import numpy as np 

def function(x):

	n3 = 6
	e2 = x
	paths = []
	try:
		if e2 <= 2:
			e2 = 9+e2
			e2 = 2*e2
			paths.append(1)
		else:
			n3 = n3/n3
			paths.append(2)
		if n3 >= 0:
			n3 = x+3
			paths.append(3)
		else:
			e2 = e2*7
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))