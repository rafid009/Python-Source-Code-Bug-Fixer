import numpy as np 

def function(x):

	k4 = x
	j0 = 8
	x = 1
	paths = []
	try:
		if k4 > 4:
			x = x*9
			k4 = 9+2
			paths.append(1)
		else:
			x = 1-2
			j0 = k4*j0
			paths.append(2)
		if x < 4:
			k4 = k4/8
			j0 = 6-j0
			k4 = 6/k4
			paths.append(3)
		else:
			k4 = k4+9
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		x = j0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))