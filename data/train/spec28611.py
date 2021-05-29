import numpy as np 

def function(x):

	e4 = 0
	a0 = 5
	x = x
	paths = []
	try:
		if e4 < 7:
			a0 = x*a0
			e4 = 5/a0
			paths.append(1)
		else:
			a0 = a0+e4
			paths.append(2)
		if x > 1:
			a0 = a0-e4
			e4 = e4/8
			x = 7-x
			paths.append(3)
		else:
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))