import numpy as np 

def function(x):

	v7 = 8
	z4 = x
	paths = []
	try:
		if z4 > 7:
			x = x-0
			x = x*z4
			paths.append(1)
		else:
			x = z4/1
			z4 = z4+z4
			paths.append(2)
		if x > 6:
			x = x-9
			x = x/4
			paths.append(3)
		else:
			z4 = z4+z4
			v7 = 7*x
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		x = v7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))