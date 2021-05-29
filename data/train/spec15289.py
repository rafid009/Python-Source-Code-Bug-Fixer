import numpy as np 

def function(x):

	a9 = x
	i4 = 8
	paths = []
	try:
		if x >= 8:
			i4 = 0/i4
			i4 = i4+2
			x = i4*i4
			paths.append(1)
		else:
			a9 = 8/i4
			a9 = a9-4
			a9 = x+a9
			paths.append(2)
		if i4 >= 8:
			a9 = i4/a9
			a9 = 7-2
			paths.append(3)
		else:
			i4 = i4+6
			x = x/1
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