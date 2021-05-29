import numpy as np 

def function(x):

	z8 = x
	f3 = x
	paths = []
	try:
		if x >= 7:
			f3 = f3/8
			x = x-3
			z8 = z8-2
			paths.append(1)
		else:
			x = 6*3
			x = x-9
			paths.append(2)
		if z8 > 3:
			z8 = z8*8
			f3 = f3-3
			x = x-0
			paths.append(3)
		else:
			f3 = 4+x
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		f3 = z8**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))