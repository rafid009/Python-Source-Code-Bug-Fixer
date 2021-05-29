import numpy as np 

def function(x):

	z4 = 5
	z7 = 1
	paths = []
	try:
		if z7 >= 4:
			z4 = 5-1
			z7 = z7*9
			paths.append(1)
		else:
			x = x/8
			z7 = 4*0
			paths.append(2)
		if x <= 0:
			z7 = z7-8
			z4 = z4-4
			z4 = z7*7
			paths.append(3)
		else:
			x = 6-x
			z4 = z4/4
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