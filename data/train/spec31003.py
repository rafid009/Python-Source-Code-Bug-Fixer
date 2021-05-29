import numpy as np 

def function(x):

	u1 = 7
	z4 = x
	paths = []
	try:
		if u1 <= 6:
			z4 = 5-0
			u1 = x-4
			paths.append(1)
		else:
			u1 = 0*u1
			u1 = u1+8
			u1 = u1/6
			paths.append(2)
		if u1 <= 8:
			x = x/5
			u1 = u1/2
			paths.append(3)
		else:
			z4 = z4+2
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