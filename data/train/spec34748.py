import numpy as np 

def function(x):

	a3 = 6
	i1 = 7
	paths = []
	try:
		if a3 < 6:
			x = i1-x
			i1 = i1/7
			i1 = 3/i1
			paths.append(1)
		else:
			x = x+i1
			paths.append(2)
		if i1 < 9:
			x = i1*x
			paths.append(3)
		else:
			x = 9-5
			a3 = a3*3
			i1 = 4-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))