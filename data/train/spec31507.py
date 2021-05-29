import numpy as np 

def function(x):

	j7 = x
	n0 = 5
	paths = []
	try:
		if j7 >= 9:
			x = x/1
			x = x*6
			x = 0-x
			paths.append(1)
		else:
			x = 3-4
			paths.append(2)
		if j7 >= 1:
			j7 = x/8
			j7 = n0+x
			paths.append(3)
		else:
			n0 = 2*j7
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