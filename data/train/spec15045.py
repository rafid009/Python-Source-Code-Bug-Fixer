import numpy as np 

def function(x):

	z8 = 6
	q1 = 5
	paths = []
	try:
		if z8 < 3:
			z8 = z8-z8
			q1 = x-q1
			q1 = q1*8
			paths.append(1)
		else:
			z8 = z8*5
			x = 3+x
			z8 = 0*1
			paths.append(2)
		if z8 > 7:
			x = x/2
			z8 = 0-z8
			q1 = 8*x
			paths.append(3)
		else:
			q1 = 7+2
			q1 = x-q1
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		x = q1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))