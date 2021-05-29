import numpy as np 

def function(x):

	e6 = x
	z4 = 5
	paths = []
	try:
		if e6 < 6:
			z4 = z4+4
			e6 = e6*1
			x = 7+x
			paths.append(1)
		else:
			z4 = z4*2
			z4 = z4*1
			paths.append(2)
		if e6 > 0:
			x = 9/x
			z4 = 9*z4
			e6 = e6-1
			paths.append(3)
		else:
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))