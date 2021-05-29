import numpy as np 

def function(x):

	j9 = x
	a3 = 0
	paths = []
	try:
		if a3 > 2:
			j9 = j9*j9
			j9 = 4*x
			paths.append(1)
		else:
			j9 = j9-x
			a3 = a3*a3
			paths.append(2)
		if x >= 3:
			j9 = 0*j9
			paths.append(3)
		else:
			x = x+6
			j9 = j9-4
			a3 = j9*j9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))