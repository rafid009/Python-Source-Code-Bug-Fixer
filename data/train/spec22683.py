import numpy as np 

def function(x):

	x0 = x
	j2 = 5
	paths = []
	try:
		if x >= 8:
			x0 = 9+x0
			x = 5/x
			x0 = 6/x
			paths.append(1)
		else:
			x0 = x0-j2
			paths.append(2)
		if x >= 5:
			j2 = 5*j2
			x = 4+x
			x0 = x0-4
			paths.append(3)
		else:
			x0 = x+9
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x0 = x0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))