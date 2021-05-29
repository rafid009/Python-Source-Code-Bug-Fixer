import numpy as np 

def function(x):

	a5 = x
	j0 = x
	paths = []
	try:
		if a5 <= 8:
			j0 = j0*a5
			x = j0/x
			paths.append(1)
		else:
			j0 = 1+j0
			a5 = 3+a5
			paths.append(2)
		if a5 >= 6:
			a5 = 2/x
			paths.append(3)
		else:
			x = 3-8
			j0 = j0*j0
			a5 = a5-0
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))