import numpy as np 

def function(x):

	a3 = 9
	n9 = x
	paths = []
	try:
		if x > 7:
			x = n9+2
			a3 = n9+0
			x = 8-a3
			paths.append(1)
		else:
			n9 = n9/a3
			n9 = x+2
			x = x-x
			paths.append(2)
		if a3 > 4:
			n9 = 9/n9
			paths.append(3)
		else:
			x = a3-a3
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