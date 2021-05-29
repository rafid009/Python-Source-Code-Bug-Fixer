import numpy as np 

def function(x):

	x5 = x
	z9 = x
	paths = []
	try:
		if x5 > 9:
			x = x/6
			x5 = 3+x5
			paths.append(1)
		else:
			z9 = x/z9
			x = z9+x
			x = x+z9
			paths.append(2)
		if x5 > 7:
			z9 = 0-z9
			x5 = x5+2
			x = x*z9
			paths.append(3)
		else:
			x5 = x5-7
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		x = z9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))