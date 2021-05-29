import numpy as np 

def function(x):

	b2 = x
	z1 = x
	paths = []
	try:
		if x < 6:
			z1 = 1+x
			b2 = 0+z1
			b2 = b2-5
			paths.append(1)
		else:
			z1 = z1/b2
			paths.append(2)
		if b2 < 4:
			z1 = 5-1
			paths.append(3)
		else:
			b2 = b2*0
			x = x/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))