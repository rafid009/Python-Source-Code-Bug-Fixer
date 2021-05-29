import numpy as np 

def function(x):

	v1 = 2
	b0 = 0
	paths = []
	try:
		if x <= 6:
			b0 = 3/6
			v1 = 7+v1
			b0 = b0-x
			paths.append(1)
		else:
			v1 = v1-5
			paths.append(2)
		if x >= 3:
			x = x-3
			b0 = b0*5
			paths.append(3)
		else:
			x = 4*8
			b0 = 4-5
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		v1 = b0**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))