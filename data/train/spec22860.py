import numpy as np 

def function(x):

	b2 = 1
	z8 = 7
	paths = []
	try:
		if b2 < 5:
			x = 3/x
			x = x+7
			paths.append(1)
		else:
			x = x+9
			z8 = 6-z8
			z8 = 7/4
			paths.append(2)
		if b2 >= 4:
			x = 0/6
			z8 = x-0
			paths.append(3)
		else:
			x = 7-x
			z8 = b2/x
			b2 = b2-2
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		b2 = b2**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))