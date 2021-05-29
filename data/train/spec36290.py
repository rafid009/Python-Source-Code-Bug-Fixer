import numpy as np 

def function(x):

	n3 = x
	n6 = x
	paths = []
	try:
		if n3 >= 2:
			n6 = n6*n6
			paths.append(1)
		else:
			x = x+n6
			n3 = 4/n3
			n6 = n6-0
			paths.append(2)
		if n6 > 1:
			x = n6-x
			paths.append(3)
		else:
			n3 = 7*n3
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		n6 = n3**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))