import numpy as np 

def function(x):

	e9 = x
	z9 = 0
	paths = []
	try:
		if z9 < 2:
			x = x+e9
			paths.append(1)
		else:
			x = 1+x
			z9 = 9/z9
			e9 = 4-e9
			paths.append(2)
		if e9 < 0:
			z9 = z9-7
			z9 = z9+2
			x = x-7
			paths.append(3)
		else:
			x = 3*z9
			x = x+1
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		e9 = z9**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))