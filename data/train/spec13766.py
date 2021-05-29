import numpy as np 

def function(x):

	b6 = 3
	z4 = x
	paths = []
	try:
		if z4 <= 5:
			b6 = b6+b6
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if b6 > 0:
			b6 = b6-7
			z4 = z4/2
			z4 = z4*3
			paths.append(3)
		else:
			x = 4-x
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