import numpy as np 

def function(x):

	v9 = x
	n9 = x
	paths = []
	try:
		if v9 > 4:
			x = x/x
			v9 = x/n9
			paths.append(1)
		else:
			n9 = x-3
			x = x-9
			n9 = 8+n9
			paths.append(2)
		if x > 0:
			x = n9*5
			v9 = 3+v9
			paths.append(3)
		else:
			v9 = v9+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))