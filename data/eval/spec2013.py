import numpy as np 

def function(x):

	x1 = x
	i4 = x
	paths = []
	try:
		if i4 > 2:
			x = 1*x
			i4 = 0*x1
			paths.append(1)
		else:
			x1 = 5*x1
			paths.append(2)
		if x > 4:
			x = 0/x
			x1 = 2*x1
			x1 = 2*x
			paths.append(3)
		else:
			i4 = i4-3
			x = x+4
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x1 = x1**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))