import numpy as np 

def function(x):

	f0 = 7
	z7 = 0
	paths = []
	try:
		if x >= 0:
			f0 = 2/f0
			z7 = z7-x
			paths.append(1)
		else:
			x = x*f0
			z7 = 8+x
			paths.append(2)
		if z7 <= 0:
			z7 = z7/5
			f0 = f0+6
			paths.append(3)
		else:
			f0 = f0*6
			z7 = z7-f0
			z7 = z7*x
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		f0 = z7**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))