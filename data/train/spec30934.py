import numpy as np 

def function(x):

	v5 = 4
	a9 = 8
	paths = []
	try:
		if a9 > 0:
			v5 = 0+a9
			a9 = a9+6
			paths.append(1)
		else:
			x = x*a9
			v5 = v5-0
			paths.append(2)
		if v5 >= 2:
			a9 = 9-a9
			paths.append(3)
		else:
			v5 = v5/v5
			x = 9*x
			a9 = a9/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))