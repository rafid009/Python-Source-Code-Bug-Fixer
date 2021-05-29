import numpy as np 

def function(x):

	l0 = 6
	i4 = x
	paths = []
	try:
		if l0 >= 0:
			l0 = 6*x
			paths.append(1)
		else:
			l0 = 5*i4
			x = 8-x
			paths.append(2)
		if l0 <= 8:
			x = x-3
			i4 = x+x
			paths.append(3)
		else:
			l0 = x-l0
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))