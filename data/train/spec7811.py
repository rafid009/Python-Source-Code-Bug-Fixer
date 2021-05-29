import numpy as np 

def function(x):

	i1 = 8
	y1 = 2
	x = x
	paths = []
	try:
		if i1 >= 5:
			y1 = y1+i1
			x = 8/x
			paths.append(1)
		else:
			i1 = 4-8
			x = x+7
			i1 = i1+2
			paths.append(2)
		if i1 >= 5:
			y1 = 9/y1
			i1 = 3+i1
			i1 = i1/i1
			paths.append(3)
		else:
			i1 = 4-8
			y1 = y1-y1
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