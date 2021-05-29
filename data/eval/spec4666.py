import numpy as np 

def function(x):

	z4 = 9
	b6 = x
	paths = []
	try:
		if b6 < 7:
			z4 = b6+x
			x = x+x
			paths.append(1)
		else:
			z4 = x-z4
			paths.append(2)
		if x > 5:
			z4 = 0*2
			z4 = 4+x
			paths.append(3)
		else:
			x = x*x
			b6 = b6/b6
			x = x-2
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))