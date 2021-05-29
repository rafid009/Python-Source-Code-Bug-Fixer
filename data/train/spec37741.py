import numpy as np 

def function(x):

	z0 = x
	j8 = 4
	paths = []
	try:
		if z0 < 4:
			x = x*x
			paths.append(1)
		else:
			x = x*9
			x = 4*x
			paths.append(2)
		if j8 >= 1:
			j8 = 0*4
			j8 = 7-j8
			paths.append(3)
		else:
			x = 3+5
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		z0 = z0**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))