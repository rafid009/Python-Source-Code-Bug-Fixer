import numpy as np 

def function(x):

	v6 = 4
	j0 = 6
	paths = []
	try:
		if j0 <= 2:
			j0 = j0/5
			v6 = v6-6
			x = 7-v6
			paths.append(1)
		else:
			j0 = j0+j0
			paths.append(2)
		if v6 >= 2:
			x = 6/x
			paths.append(3)
		else:
			x = 7*x
			j0 = x*j0
			v6 = 9-x
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