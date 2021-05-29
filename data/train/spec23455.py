import numpy as np 

def function(x):

	z9 = 0
	l1 = 2
	paths = []
	try:
		if z9 < 1:
			z9 = z9+x
			paths.append(1)
		else:
			x = 1+x
			paths.append(2)
		if x < 0:
			z9 = l1/z9
			l1 = 6+l1
			paths.append(3)
		else:
			z9 = z9/9
			l1 = l1/9
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		l1 = z9**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))