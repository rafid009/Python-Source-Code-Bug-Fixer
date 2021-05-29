import numpy as np 

def function(x):

	x0 = 8
	z9 = x
	paths = []
	try:
		if z9 <= 6:
			x0 = 5+7
			x0 = x0+8
			paths.append(1)
		else:
			x = x+6
			x = x*x0
			z9 = z9-4
			paths.append(2)
		if x0 <= 3:
			z9 = z9/2
			x = 0*x
			paths.append(3)
		else:
			x0 = z9-6
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		x0 = z9**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))