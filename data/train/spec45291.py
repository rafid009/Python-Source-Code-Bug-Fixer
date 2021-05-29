import numpy as np 

def function(x):

	j0 = x
	v4 = x
	x = 4
	paths = []
	try:
		if v4 <= 2:
			v4 = j0/v4
			paths.append(1)
		else:
			j0 = 5*6
			x = x+6
			v4 = j0-v4
			paths.append(2)
		if v4 <= 0:
			x = 0*x
			paths.append(3)
		else:
			x = 0-x
			j0 = 6-j0
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		x = v4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))