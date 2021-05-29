import numpy as np 

def function(x):

	b2 = 5
	z8 = 4
	paths = []
	try:
		if x < 3:
			b2 = x+3
			b2 = 8/b2
			paths.append(1)
		else:
			z8 = z8-4
			paths.append(2)
		if z8 <= 2:
			x = x+1
			z8 = 7*z8
			paths.append(3)
		else:
			b2 = b2*b2
			z8 = z8-0
			z8 = x*9
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		b2 = z8**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))