import numpy as np 

def function(x):

	j8 = x
	n0 = x
	paths = []
	try:
		if x <= 3:
			n0 = n0*1
			x = x/x
			j8 = x-x
			paths.append(1)
		else:
			n0 = n0+3
			x = x-5
			paths.append(2)
		if n0 < 2:
			x = x/4
			n0 = n0-3
			j8 = 9*j8
			paths.append(3)
		else:
			n0 = n0-3
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		j8 = n0**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))