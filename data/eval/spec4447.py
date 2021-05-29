import numpy as np 

def function(x):

	n9 = x
	n6 = 5
	paths = []
	try:
		if n6 < 9:
			n9 = 9/n9
			n6 = n9+n9
			paths.append(1)
		else:
			n9 = x/2
			n9 = 4-n9
			paths.append(2)
		if n6 < 1:
			n6 = 9/3
			n9 = 0-n9
			paths.append(3)
		else:
			n6 = n6/x
			x = n9/2
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		x = n9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))