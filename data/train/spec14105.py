import numpy as np 

def function(x):

	a5 = 3
	z2 = 4
	paths = []
	try:
		if x < 4:
			z2 = z2-6
			x = x+z2
			x = x/3
			paths.append(1)
		else:
			z2 = 2*x
			z2 = 6-z2
			paths.append(2)
		if a5 >= 7:
			z2 = 8+1
			paths.append(3)
		else:
			x = 3*x
			x = x/5
			x = x*a5
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		x = z2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))