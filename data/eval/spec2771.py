import numpy as np 

def function(x):

	i4 = 4
	x0 = x
	paths = []
	try:
		if i4 > 1:
			i4 = 7/x
			x = x+x
			i4 = x0+8
			paths.append(1)
		else:
			i4 = 6*4
			x = 0*x
			i4 = i4+8
			paths.append(2)
		if x0 < 2:
			x = x/5
			paths.append(3)
		else:
			i4 = 3/i4
			x = 4-6
			x = x-8
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