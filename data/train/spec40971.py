import numpy as np 

def function(x):

	k4 = 8
	a0 = 6
	paths = []
	try:
		if x < 4:
			k4 = k4*3
			paths.append(1)
		else:
			a0 = 4+a0
			paths.append(2)
		if k4 < 8:
			x = 1*a0
			x = 4+6
			paths.append(3)
		else:
			a0 = a0+x
			a0 = k4*a0
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		x = a0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))