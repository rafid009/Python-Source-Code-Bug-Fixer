import numpy as np 

def function(x):

	j0 = 4
	k7 = x
	paths = []
	try:
		if k7 >= 9:
			j0 = j0*j0
			j0 = j0*j0
			x = 6+3
			paths.append(1)
		else:
			k7 = 0*k7
			j0 = j0+k7
			paths.append(2)
		if k7 < 8:
			x = x/5
			j0 = 4+k7
			j0 = 7/j0
			paths.append(3)
		else:
			j0 = j0-0
			k7 = k7+3
			k7 = 8/k7
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