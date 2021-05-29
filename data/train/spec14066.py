import numpy as np 

def function(x):

	z9 = 9
	x2 = x
	paths = []
	try:
		if x2 <= 3:
			x = x-5
			x2 = z9*x2
			z9 = z9/x2
			paths.append(1)
		else:
			z9 = x/4
			x2 = x2/9
			paths.append(2)
		if z9 >= 5:
			x2 = x2*x
			z9 = z9/5
			z9 = 3-8
			paths.append(3)
		else:
			x = x-9
			x2 = 2-x2
			x2 = x2-x2
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