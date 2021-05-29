import numpy as np 

def function(x):

	y7 = 6
	z7 = 9
	paths = []
	try:
		if y7 >= 8:
			x = 0*0
			paths.append(1)
		else:
			x = x/3
			z7 = x-z7
			z7 = y7/z7
			paths.append(2)
		if y7 > 7:
			z7 = z7*1
			paths.append(3)
		else:
			z7 = 2/z7
			x = 8/x
			y7 = x-y7
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		y7 = y7**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))