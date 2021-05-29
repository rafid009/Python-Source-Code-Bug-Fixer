import numpy as np 

def function(x):

	a4 = 7
	i0 = 3
	paths = []
	try:
		if a4 >= 6:
			x = i0*x
			i0 = i0-1
			paths.append(1)
		else:
			i0 = i0+4
			i0 = i0-i0
			i0 = i0*i0
			paths.append(2)
		if x >= 5:
			i0 = i0+2
			x = x*a4
			i0 = 0/i0
			paths.append(3)
		else:
			i0 = 5/i0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))