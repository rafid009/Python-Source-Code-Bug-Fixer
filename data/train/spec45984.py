import numpy as np 

def function(x):

	z1 = 6
	k5 = 0
	paths = []
	try:
		if z1 <= 8:
			z1 = 6-6
			z1 = 3-2
			paths.append(1)
		else:
			z1 = z1*x
			paths.append(2)
		if k5 < 3:
			k5 = k5-x
			z1 = z1+2
			paths.append(3)
		else:
			z1 = x/z1
			z1 = z1*0
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		x = k5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))