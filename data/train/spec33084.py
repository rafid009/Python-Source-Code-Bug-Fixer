import numpy as np 

def function(x):

	z8 = 9
	i5 = x
	paths = []
	try:
		if i5 < 9:
			z8 = i5/5
			i5 = i5-0
			x = z8-4
			paths.append(1)
		else:
			x = 5+7
			i5 = 2*i5
			paths.append(2)
		if z8 >= 0:
			z8 = z8+z8
			i5 = i5/9
			x = x+2
			paths.append(3)
		else:
			i5 = 1/i5
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))