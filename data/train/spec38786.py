import numpy as np 

def function(x):

	q0 = 0
	u1 = x
	paths = []
	try:
		if u1 > 2:
			x = x-9
			x = x+4
			paths.append(1)
		else:
			x = 3/x
			u1 = 7/4
			x = u1/u1
			paths.append(2)
		if u1 > 0:
			x = q0+x
			u1 = q0-9
			u1 = 7+9
			paths.append(3)
		else:
			u1 = u1/9
			x = 3*8
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