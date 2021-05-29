import numpy as np 

def function(x):

	z4 = x
	u1 = x
	paths = []
	try:
		if x < 4:
			z4 = z4*2
			x = x-x
			paths.append(1)
		else:
			u1 = 2-8
			z4 = 8*9
			u1 = u1*x
			paths.append(2)
		if u1 >= 3:
			u1 = u1-8
			x = x/u1
			z4 = z4/u1
			paths.append(3)
		else:
			u1 = 0+1
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))