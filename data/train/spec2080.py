import numpy as np 

def function(x):

	z7 = 8
	f1 = x
	paths = []
	try:
		if f1 >= 5:
			x = x*5
			paths.append(1)
		else:
			z7 = f1*3
			z7 = z7-f1
			x = f1+2
			paths.append(2)
		if f1 < 9:
			z7 = f1+7
			z7 = 3*z7
			paths.append(3)
		else:
			z7 = 2-z7
			f1 = 3-3
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		x = z7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))