import numpy as np 

def function(x):

	z4 = x
	l9 = 4
	paths = []
	try:
		if x >= 0:
			l9 = l9+6
			paths.append(1)
		else:
			l9 = 4*l9
			l9 = l9*2
			paths.append(2)
		if l9 > 0:
			l9 = 7*7
			paths.append(3)
		else:
			z4 = z4+1
			l9 = l9/5
			x = 7+6
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))