import numpy as np 

def function(x):

	z1 = x
	u1 = 7
	paths = []
	try:
		if x < 1:
			x = 9+u1
			x = z1*8
			x = z1/7
			paths.append(1)
		else:
			u1 = 0*u1
			x = 3/x
			u1 = 2*u1
			paths.append(2)
		if u1 > 9:
			u1 = u1-2
			paths.append(3)
		else:
			z1 = 3-u1
			u1 = u1/2
			x = x-z1
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		x = z1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))