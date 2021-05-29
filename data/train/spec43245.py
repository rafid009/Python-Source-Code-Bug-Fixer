import numpy as np 

def function(x):

	a0 = 7
	e4 = x
	paths = []
	try:
		if x < 5:
			a0 = 6*a0
			x = 8/e4
			e4 = 4-x
			paths.append(1)
		else:
			a0 = 0/a0
			e4 = 9/9
			a0 = 1*9
			paths.append(2)
		if a0 <= 9:
			e4 = 6-e4
			e4 = 7+5
			a0 = a0-a0
			paths.append(3)
		else:
			a0 = 3*a0
			a0 = a0+3
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