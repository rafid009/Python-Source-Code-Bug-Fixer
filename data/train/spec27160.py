import numpy as np 

def function(x):

	x9 = 4
	z4 = x
	paths = []
	try:
		if z4 <= 0:
			x = 8*5
			z4 = 6/z4
			paths.append(1)
		else:
			x9 = 8*0
			x9 = x9+2
			z4 = 1+x9
			paths.append(2)
		if x < 9:
			x = x-1
			z4 = 1+x
			x = x+0
			paths.append(3)
		else:
			x = x-3
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		x9 = z4**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))