import numpy as np 

def function(x):

	z9 = x
	l2 = x
	x = 7
	paths = []
	try:
		if x <= 3:
			l2 = l2+3
			paths.append(1)
		else:
			z9 = 2-z9
			l2 = 2*l2
			z9 = 5-8
			paths.append(2)
		if z9 < 7:
			z9 = z9-2
			z9 = 2+z9
			l2 = z9*2
			paths.append(3)
		else:
			z9 = x+z9
			z9 = z9*5
			l2 = l2+9
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		z9 = z9**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))