import numpy as np 

def function(x):

	l9 = x
	z7 = 9
	paths = []
	try:
		if x < 2:
			l9 = l9+8
			paths.append(1)
		else:
			z7 = 1-z7
			paths.append(2)
		if l9 < 6:
			l9 = l9*z7
			x = x-x
			paths.append(3)
		else:
			l9 = l9+x
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		l9 = l9**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))