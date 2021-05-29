import numpy as np 

def function(x):

	z2 = x
	f8 = 2
	paths = []
	try:
		if x > 6:
			z2 = 4/7
			paths.append(1)
		else:
			x = x*0
			x = x+x
			paths.append(2)
		if z2 > 3:
			z2 = f8*x
			paths.append(3)
		else:
			x = x-0
			z2 = 6*z2
			x = 3*4
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