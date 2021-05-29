import numpy as np 

def function(x):

	z7 = x
	b0 = 9
	paths = []
	try:
		if x < 7:
			x = x+b0
			x = z7-b0
			z7 = 0-8
			paths.append(1)
		else:
			x = 4-4
			z7 = z7*0
			paths.append(2)
		if x > 4:
			b0 = b0-z7
			z7 = 0*b0
			paths.append(3)
		else:
			b0 = 3-b0
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		z7 = z7**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))