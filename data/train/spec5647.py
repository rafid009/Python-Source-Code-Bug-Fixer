import numpy as np 

def function(x):

	z4 = x
	b3 = 4
	paths = []
	try:
		if b3 <= 3:
			b3 = z4/4
			paths.append(1)
		else:
			z4 = z4/1
			x = 3+z4
			b3 = b3+x
			paths.append(2)
		if b3 <= 9:
			z4 = z4-6
			paths.append(3)
		else:
			x = x-x
			b3 = b3/4
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		z4 = b3**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))