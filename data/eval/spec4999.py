import numpy as np 

def function(x):

	i4 = 5
	q7 = x
	paths = []
	try:
		if i4 >= 0:
			q7 = i4-q7
			paths.append(1)
		else:
			i4 = i4-2
			q7 = x+2
			paths.append(2)
		if i4 >= 8:
			x = x-8
			paths.append(3)
		else:
			i4 = x/6
			i4 = 4-3
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