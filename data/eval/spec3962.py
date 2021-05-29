import numpy as np 

def function(x):

	l4 = x
	z9 = x
	paths = []
	try:
		if l4 <= 9:
			l4 = l4*1
			z9 = 9+z9
			paths.append(1)
		else:
			z9 = z9+l4
			paths.append(2)
		if l4 > 5:
			l4 = l4+l4
			z9 = z9+5
			paths.append(3)
		else:
			l4 = 3*l4
			z9 = 3-3
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))