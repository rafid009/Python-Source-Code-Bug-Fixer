import numpy as np 

def function(x):

	n9 = 3
	a1 = x
	paths = []
	try:
		if n9 <= 0:
			x = 0-1
			n9 = n9*7
			paths.append(1)
		else:
			n9 = 4*6
			n9 = 7/3
			paths.append(2)
		if n9 >= 1:
			x = n9/3
			a1 = a1/2
			paths.append(3)
		else:
			n9 = n9+3
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		n9 = a1**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))