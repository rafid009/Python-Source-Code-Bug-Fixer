import numpy as np 

def function(x):

	a6 = x
	f9 = x
	paths = []
	try:
		if a6 >= 9:
			x = x/a6
			a6 = 1-6
			x = x/8
			paths.append(1)
		else:
			x = x/1
			f9 = x*6
			paths.append(2)
		if x >= 7:
			a6 = 9-a6
			paths.append(3)
		else:
			a6 = 7*f9
			a6 = a6/a6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))