import numpy as np 

def function(x):

	e5 = 2
	a0 = 5
	x = x
	paths = []
	try:
		if e5 >= 3:
			x = a0/x
			a0 = a0/a0
			e5 = 8-a0
			paths.append(1)
		else:
			a0 = 1-e5
			x = x/a0
			e5 = e5*3
			paths.append(2)
		if x >= 8:
			x = x/e5
			paths.append(3)
		else:
			x = x-8
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