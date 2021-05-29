import numpy as np 

def function(x):

	z6 = 6
	b6 = 9
	paths = []
	try:
		if b6 > 0:
			b6 = b6-z6
			z6 = z6/1
			paths.append(1)
		else:
			z6 = z6*b6
			b6 = b6+1
			paths.append(2)
		if z6 <= 3:
			z6 = 4/2
			z6 = z6-b6
			paths.append(3)
		else:
			z6 = x*3
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))