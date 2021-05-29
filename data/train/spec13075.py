import numpy as np 

def function(x):

	i1 = x
	y0 = 4
	paths = []
	try:
		if y0 >= 6:
			i1 = i1-3
			paths.append(1)
		else:
			y0 = x+y0
			i1 = 8/i1
			i1 = 1-2
			paths.append(2)
		if y0 > 8:
			x = 1*x
			y0 = y0*7
			paths.append(3)
		else:
			x = x*i1
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x = i1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))