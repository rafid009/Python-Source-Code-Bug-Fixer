import numpy as np 

def function(x):

	a3 = x
	i1 = x
	paths = []
	try:
		if a3 < 7:
			i1 = 8/i1
			i1 = 4*5
			paths.append(1)
		else:
			x = 2/i1
			i1 = i1+3
			paths.append(2)
		if i1 > 6:
			i1 = i1/x
			x = i1+a3
			paths.append(3)
		else:
			a3 = a3*6
			i1 = 8-i1
			i1 = x/i1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i1 = x**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))