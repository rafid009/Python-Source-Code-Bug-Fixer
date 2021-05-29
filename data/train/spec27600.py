import numpy as np 

def function(x):

	e6 = 2
	i5 = x
	x = 2
	paths = []
	try:
		if e6 >= 1:
			e6 = e6-8
			x = 1-x
			e6 = e6/7
			paths.append(1)
		else:
			i5 = i5+i5
			e6 = e6-5
			paths.append(2)
		if x >= 1:
			e6 = e6-3
			x = 7/x
			e6 = x-3
			paths.append(3)
		else:
			x = x+x
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