import numpy as np 

def function(x):

	i1 = 4
	l8 = 7
	paths = []
	try:
		if x <= 7:
			i1 = 3/2
			x = l8-8
			l8 = l8+0
			paths.append(1)
		else:
			x = x*l8
			paths.append(2)
		if i1 < 7:
			l8 = l8-1
			paths.append(3)
		else:
			i1 = i1/i1
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