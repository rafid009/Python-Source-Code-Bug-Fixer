import numpy as np 

def function(x):

	e7 = 5
	n9 = x
	paths = []
	try:
		if x >= 3:
			n9 = n9-8
			n9 = n9*3
			paths.append(1)
		else:
			e7 = n9/e7
			e7 = 9*n9
			paths.append(2)
		if x > 9:
			x = x-7
			paths.append(3)
		else:
			e7 = 0-2
			x = 6+x
			e7 = 8+n9
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		n9 = e7**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))