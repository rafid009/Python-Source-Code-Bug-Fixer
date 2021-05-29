import numpy as np 

def function(x):

	u1 = 8
	b0 = x
	x = 1
	paths = []
	try:
		if b0 >= 0:
			u1 = u1-4
			paths.append(1)
		else:
			x = u1/4
			paths.append(2)
		if b0 < 0:
			u1 = 3-u1
			paths.append(3)
		else:
			b0 = 4-4
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		u1 = u1**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))