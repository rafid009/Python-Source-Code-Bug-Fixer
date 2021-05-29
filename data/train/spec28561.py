import numpy as np 

def function(x):

	v7 = 6
	a5 = 2
	paths = []
	try:
		if a5 < 5:
			a5 = v7-a5
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if a5 <= 3:
			a5 = a5-a5
			x = 4*x
			paths.append(3)
		else:
			v7 = 1-v7
			x = x-9
			a5 = 0*a5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))