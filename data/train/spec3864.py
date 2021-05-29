import numpy as np 

def function(x):

	f8 = 5
	z9 = 4
	paths = []
	try:
		if f8 > 1:
			z9 = f8/z9
			paths.append(1)
		else:
			f8 = 3*7
			paths.append(2)
		if z9 >= 4:
			x = x+z9
			x = z9*6
			paths.append(3)
		else:
			x = x*2
			f8 = 7-f8
			f8 = f8-x
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