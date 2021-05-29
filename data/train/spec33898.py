import numpy as np 

def function(x):

	z4 = 7
	e4 = x
	paths = []
	try:
		if z4 <= 3:
			e4 = 0*8
			z4 = x-8
			paths.append(1)
		else:
			x = x-2
			e4 = e4-5
			z4 = 8/z4
			paths.append(2)
		if e4 <= 5:
			x = x*e4
			paths.append(3)
		else:
			x = 3/9
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		e4 = e4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))