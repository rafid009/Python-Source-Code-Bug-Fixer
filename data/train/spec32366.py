import numpy as np 

def function(x):

	z4 = x
	u1 = 5
	paths = []
	try:
		if u1 >= 6:
			u1 = u1-u1
			u1 = z4/1
			z4 = z4*0
			paths.append(1)
		else:
			z4 = u1-z4
			u1 = x*9
			u1 = u1-1
			paths.append(2)
		if u1 > 5:
			z4 = 1+2
			x = x/u1
			x = 1+x
			paths.append(3)
		else:
			x = x+x
			x = 7/x
			u1 = 2*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))