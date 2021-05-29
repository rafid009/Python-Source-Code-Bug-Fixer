import numpy as np 

def function(x):

	a9 = 7
	n1 = x
	paths = []
	try:
		if a9 <= 3:
			a9 = a9-1
			n1 = 6-n1
			x = 9+x
			paths.append(1)
		else:
			x = x*5
			x = x+x
			paths.append(2)
		if n1 <= 1:
			a9 = n1/a9
			paths.append(3)
		else:
			a9 = 7/1
			x = 1/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))