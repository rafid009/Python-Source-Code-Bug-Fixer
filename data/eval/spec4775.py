import numpy as np 

def function(x):

	z7 = 4
	o8 = x
	paths = []
	try:
		if o8 >= 7:
			z7 = z7/5
			x = x/3
			o8 = z7*2
			paths.append(1)
		else:
			o8 = o8*3
			z7 = 7-z7
			x = z7-6
			paths.append(2)
		if z7 > 7:
			z7 = z7-1
			o8 = 6-x
			z7 = z7-z7
			paths.append(3)
		else:
			z7 = o8+z7
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