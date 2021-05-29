import numpy as np 

def function(x):

	a5 = x
	e0 = x
	paths = []
	try:
		if a5 >= 2:
			a5 = a5*x
			paths.append(1)
		else:
			x = a5*7
			e0 = e0/a5
			paths.append(2)
		if a5 > 8:
			x = 4+x
			paths.append(3)
		else:
			a5 = x/1
			x = x-5
			e0 = 3/x
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))