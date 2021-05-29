import numpy as np 

def function(x):

	n0 = 0
	j8 = x
	paths = []
	try:
		if x >= 0:
			x = n0/x
			paths.append(1)
		else:
			n0 = n0/9
			j8 = j8+1
			paths.append(2)
		if j8 < 6:
			j8 = j8/2
			n0 = n0*6
			n0 = n0-j8
			paths.append(3)
		else:
			j8 = j8*5
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))