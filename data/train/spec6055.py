import numpy as np 

def function(x):

	o7 = x
	z9 = x
	paths = []
	try:
		if z9 < 4:
			o7 = o7-4
			z9 = 9/8
			paths.append(1)
		else:
			o7 = o7+1
			z9 = 2-z9
			x = x+7
			paths.append(2)
		if z9 <= 7:
			x = z9-x
			paths.append(3)
		else:
			z9 = z9*8
			x = z9+6
			x = x/2
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		x = o7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))