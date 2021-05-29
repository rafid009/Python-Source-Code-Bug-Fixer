import numpy as np 

def function(x):

	z6 = x
	u1 = 4
	paths = []
	try:
		if x <= 0:
			u1 = 7/u1
			u1 = 9+z6
			x = u1/u1
			paths.append(1)
		else:
			u1 = 9*u1
			paths.append(2)
		if u1 <= 9:
			u1 = x*u1
			x = z6-8
			paths.append(3)
		else:
			u1 = 1-u1
			u1 = 4/u1
			x = x*x
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