import numpy as np 

def function(x):

	u1 = x
	j0 = x
	paths = []
	try:
		if j0 >= 4:
			j0 = 8/j0
			x = 3*j0
			paths.append(1)
		else:
			x = 5-x
			paths.append(2)
		if j0 > 9:
			x = 8-5
			j0 = 4+j0
			j0 = 3-j0
			paths.append(3)
		else:
			u1 = 2+u1
			u1 = 4-u1
			u1 = x/u1
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		x = j0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))