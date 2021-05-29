import numpy as np 

def function(x):

	b2 = 8
	z9 = 0
	paths = []
	try:
		if b2 <= 1:
			b2 = x-7
			paths.append(1)
		else:
			b2 = x+7
			x = 1*x
			paths.append(2)
		if z9 >= 4:
			z9 = 4-z9
			z9 = z9/6
			paths.append(3)
		else:
			x = 1-x
			z9 = 3*b2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))