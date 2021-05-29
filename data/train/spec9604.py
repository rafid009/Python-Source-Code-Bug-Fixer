import numpy as np 

def function(x):

	u6 = x
	z1 = x
	paths = []
	try:
		if x < 5:
			u6 = u6+8
			z1 = x+5
			paths.append(1)
		else:
			z1 = z1/4
			paths.append(2)
		if u6 >= 0:
			x = x/u6
			u6 = u6*1
			x = 6/z1
			paths.append(3)
		else:
			z1 = z1+z1
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		z1 = u6**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))