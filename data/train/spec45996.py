import numpy as np 

def function(x):

	z4 = 8
	k3 = 0
	paths = []
	try:
		if x >= 4:
			x = x-k3
			x = x*3
			paths.append(1)
		else:
			z4 = z4/9
			x = 4*x
			paths.append(2)
		if x >= 7:
			k3 = k3/3
			x = 5*x
			paths.append(3)
		else:
			z4 = z4+x
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		x = z4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))