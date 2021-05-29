import numpy as np 

def function(x):

	a5 = 7
	a0 = x
	paths = []
	try:
		if x < 9:
			a5 = a5/2
			paths.append(1)
		else:
			a0 = a0/x
			a5 = 3*a0
			x = a0/6
			paths.append(2)
		if a0 > 9:
			a0 = 7/a5
			paths.append(3)
		else:
			a5 = 8/a5
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