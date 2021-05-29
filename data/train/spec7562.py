import numpy as np 

def function(x):

	a8 = 6
	n7 = 3
	paths = []
	try:
		if n7 > 8:
			a8 = a8+5
			a8 = a8/a8
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if n7 >= 5:
			n7 = n7*9
			paths.append(3)
		else:
			n7 = n7-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))