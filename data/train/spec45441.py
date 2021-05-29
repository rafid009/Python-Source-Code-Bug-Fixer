import numpy as np 

def function(x):

	v5 = x
	z5 = x
	paths = []
	try:
		if x >= 5:
			z5 = 9-z5
			x = x-1
			x = 3-9
			paths.append(1)
		else:
			x = x/5
			paths.append(2)
		if x >= 2:
			z5 = v5/z5
			z5 = z5*7
			paths.append(3)
		else:
			v5 = v5+5
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		v5 = v5**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))