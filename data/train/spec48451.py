import numpy as np 

def function(x):

	z2 = x
	q9 = x
	paths = []
	try:
		if x < 8:
			x = x/x
			paths.append(1)
		else:
			z2 = 3+x
			z2 = 4*z2
			paths.append(2)
		if x > 5:
			q9 = q9+z2
			paths.append(3)
		else:
			z2 = z2*1
			x = 8*5
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		z2 = z2**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))