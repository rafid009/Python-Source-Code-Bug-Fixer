import numpy as np 

def function(x):

	e5 = 8
	n7 = x
	paths = []
	try:
		if e5 <= 1:
			x = 0/n7
			n7 = n7/n7
			paths.append(1)
		else:
			n7 = 3/n7
			e5 = e5/6
			paths.append(2)
		if e5 >= 6:
			x = e5-6
			paths.append(3)
		else:
			n7 = n7/6
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		e5 = n7**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))