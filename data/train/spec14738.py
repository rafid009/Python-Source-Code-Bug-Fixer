import numpy as np 

def function(x):

	a9 = 8
	a0 = 5
	paths = []
	try:
		if x > 1:
			x = x+a0
			a0 = a0-3
			a0 = 7+a0
			paths.append(1)
		else:
			a9 = a9*x
			a0 = 3-a0
			paths.append(2)
		if x <= 8:
			a9 = x-a9
			a9 = a9-x
			paths.append(3)
		else:
			a0 = 7/a0
			x = 4/x
			x = x/6
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))