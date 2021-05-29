import numpy as np 

def function(x):

	a0 = 4
	y4 = 9
	paths = []
	try:
		if a0 < 8:
			a0 = 1-8
			paths.append(1)
		else:
			a0 = a0-9
			paths.append(2)
		if a0 < 5:
			x = x*9
			x = x-y4
			x = x/y4
			paths.append(3)
		else:
			a0 = 6/a0
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		y4 = a0**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))