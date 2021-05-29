import numpy as np 

def function(x):

	u1 = 7
	z5 = x
	paths = []
	try:
		if z5 < 8:
			z5 = 4+z5
			paths.append(1)
		else:
			z5 = 5/z5
			x = x-8
			z5 = z5-3
			paths.append(2)
		if u1 <= 8:
			z5 = z5/8
			z5 = x/z5
			u1 = u1+z5
			paths.append(3)
		else:
			u1 = u1*2
			z5 = 2*8
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