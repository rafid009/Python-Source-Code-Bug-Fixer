import numpy as np 

def function(x):

	z1 = x
	l5 = x
	paths = []
	try:
		if x > 1:
			l5 = l5+7
			z1 = 6-9
			z1 = 5/z1
			paths.append(1)
		else:
			z1 = z1*z1
			z1 = z1/2
			x = 9+x
			paths.append(2)
		if l5 < 5:
			z1 = 7+z1
			l5 = l5*x
			paths.append(3)
		else:
			l5 = l5/l5
			l5 = l5/8
			z1 = 2*z1
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		x = l5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))