import numpy as np 

def function(x):

	z9 = 9
	f2 = 5
	paths = []
	try:
		if x >= 2:
			z9 = f2/7
			z9 = z9*0
			paths.append(1)
		else:
			z9 = z9/4
			paths.append(2)
		if z9 <= 1:
			f2 = 3*f2
			f2 = 0+f2
			paths.append(3)
		else:
			f2 = f2/9
			x = x/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))