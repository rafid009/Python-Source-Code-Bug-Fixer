import numpy as np 

def function(x):

	i1 = x
	z9 = 9
	paths = []
	try:
		if x >= 9:
			z9 = z9/4
			i1 = i1/i1
			paths.append(1)
		else:
			z9 = z9-0
			paths.append(2)
		if z9 <= 2:
			x = z9+5
			paths.append(3)
		else:
			z9 = 4/z9
			i1 = i1*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i1 = x**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))