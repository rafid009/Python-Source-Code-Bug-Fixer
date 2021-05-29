import numpy as np 

def function(x):

	i6 = x
	a4 = x
	paths = []
	try:
		if x >= 1:
			i6 = i6*x
			x = x+x
			paths.append(1)
		else:
			x = 5/i6
			x = x*a4
			x = a4-x
			paths.append(2)
		if x >= 5:
			i6 = 8/1
			a4 = x-a4
			paths.append(3)
		else:
			a4 = i6*a4
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