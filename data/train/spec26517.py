import numpy as np 

def function(x):

	n1 = x
	z7 = x
	paths = []
	try:
		if n1 <= 6:
			n1 = 1/z7
			z7 = 5-0
			paths.append(1)
		else:
			x = x/5
			z7 = 5-z7
			paths.append(2)
		if x > 4:
			x = z7/x
			n1 = z7-9
			paths.append(3)
		else:
			n1 = 0+x
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		z7 = n1**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))