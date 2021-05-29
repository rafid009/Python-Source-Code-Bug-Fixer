import numpy as np 

def function(x):

	z8 = 1
	b6 = x
	paths = []
	try:
		if z8 < 2:
			z8 = 5-z8
			paths.append(1)
		else:
			z8 = z8/9
			b6 = 7+b6
			paths.append(2)
		if b6 >= 5:
			b6 = z8*b6
			b6 = z8-b6
			b6 = 5*0
			paths.append(3)
		else:
			x = x+x
			b6 = b6/2
			x = z8/2
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))