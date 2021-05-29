import numpy as np 

def function(x):

	a7 = 9
	n6 = x
	paths = []
	try:
		if a7 <= 6:
			n6 = 4*n6
			paths.append(1)
		else:
			a7 = n6+x
			x = 8+x
			paths.append(2)
		if x <= 6:
			x = 4*n6
			x = x-x
			paths.append(3)
		else:
			x = 7+x
			a7 = 3/a7
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a7 = a7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))