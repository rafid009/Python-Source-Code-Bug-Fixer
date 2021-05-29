import numpy as np 

def function(x):

	a5 = 5
	z9 = 7
	paths = []
	try:
		if z9 < 4:
			z9 = z9*3
			a5 = a5*z9
			paths.append(1)
		else:
			x = x*6
			a5 = 5*a5
			paths.append(2)
		if x <= 5:
			a5 = z9-z9
			x = x/9
			paths.append(3)
		else:
			z9 = 6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))