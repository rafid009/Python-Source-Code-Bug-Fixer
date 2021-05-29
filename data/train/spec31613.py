import numpy as np 

def function(x):

	n9 = 3
	a4 = x
	paths = []
	try:
		if n9 >= 7:
			n9 = n9+n9
			paths.append(1)
		else:
			n9 = a4/8
			x = x+x
			x = x+7
			paths.append(2)
		if a4 > 5:
			n9 = 1+n9
			n9 = a4*n9
			paths.append(3)
		else:
			n9 = n9*7
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))