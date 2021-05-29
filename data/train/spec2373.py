import numpy as np 

def function(x):

	a6 = 7
	i1 = 4
	paths = []
	try:
		if x < 1:
			i1 = x/i1
			paths.append(1)
		else:
			i1 = i1+x
			paths.append(2)
		if i1 < 4:
			a6 = 6-9
			paths.append(3)
		else:
			i1 = x-x
			x = x/7
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