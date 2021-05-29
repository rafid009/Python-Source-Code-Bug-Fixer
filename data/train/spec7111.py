import numpy as np 

def function(x):

	z9 = 9
	n5 = x
	paths = []
	try:
		if x > 3:
			x = x*n5
			n5 = 0/6
			x = x*3
			paths.append(1)
		else:
			z9 = 4+z9
			paths.append(2)
		if n5 > 0:
			z9 = n5+n5
			x = 0/x
			x = 9*x
			paths.append(3)
		else:
			z9 = x+4
			z9 = x-9
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		x = z9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))