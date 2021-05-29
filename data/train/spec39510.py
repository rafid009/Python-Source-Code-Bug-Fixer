import numpy as np 

def function(x):

	n9 = x
	u0 = x
	paths = []
	try:
		if u0 <= 0:
			x = n9+u0
			paths.append(1)
		else:
			n9 = 4+n9
			n9 = n9+u0
			x = x+8
			paths.append(2)
		if n9 >= 3:
			n9 = 5+n9
			x = 3/x
			u0 = u0+n9
			paths.append(3)
		else:
			n9 = x+n9
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		x = u0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))