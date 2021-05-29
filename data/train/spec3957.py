import numpy as np 

def function(x):

	j0 = 8
	n3 = 3
	paths = []
	try:
		if j0 >= 8:
			n3 = j0*n3
			n3 = n3-3
			paths.append(1)
		else:
			n3 = 7/6
			x = j0*8
			n3 = 4+n3
			paths.append(2)
		if j0 >= 0:
			x = x*9
			j0 = j0/2
			paths.append(3)
		else:
			n3 = n3-2
			x = x*9
			j0 = 1*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))