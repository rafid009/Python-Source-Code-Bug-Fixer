import numpy as np 

def function(x):

	f3 = 6
	a2 = x
	paths = []
	try:
		if x >= 1:
			f3 = 5/f3
			a2 = a2/x
			paths.append(1)
		else:
			a2 = 2/5
			f3 = 3*a2
			paths.append(2)
		if a2 >= 9:
			a2 = a2/f3
			a2 = f3+3
			paths.append(3)
		else:
			f3 = f3*x
			x = x/a2
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