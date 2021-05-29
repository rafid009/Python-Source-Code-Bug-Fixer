import numpy as np 

def function(x):

	v1 = x
	j5 = x
	paths = []
	try:
		if j5 < 8:
			x = j5*4
			j5 = j5/j5
			paths.append(1)
		else:
			v1 = 4/v1
			x = 9+6
			x = 5*4
			paths.append(2)
		if j5 >= 3:
			j5 = j5/3
			x = x+7
			paths.append(3)
		else:
			j5 = x+j5
			j5 = 9-x
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