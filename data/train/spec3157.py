import numpy as np 

def function(x):

	j0 = x
	u3 = 7
	paths = []
	try:
		if x > 8:
			j0 = u3-3
			j0 = j0*j0
			paths.append(1)
		else:
			u3 = u3-u3
			paths.append(2)
		if j0 >= 0:
			u3 = j0*u3
			paths.append(3)
		else:
			j0 = 4/j0
			j0 = 9/8
			u3 = 8-j0
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