import numpy as np 

def function(x):

	z6 = x
	b1 = 3
	paths = []
	try:
		if b1 > 9:
			x = 1*x
			b1 = x*x
			z6 = x-6
			paths.append(1)
		else:
			x = x+b1
			paths.append(2)
		if z6 >= 3:
			b1 = b1+0
			paths.append(3)
		else:
			z6 = 4*3
			z6 = 4/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b1 = x**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))