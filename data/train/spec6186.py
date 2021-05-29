import numpy as np 

def function(x):

	a0 = x
	z9 = 0
	paths = []
	try:
		if a0 < 6:
			a0 = a0*1
			z9 = 5-x
			paths.append(1)
		else:
			a0 = a0/x
			z9 = 3-z9
			z9 = z9*8
			paths.append(2)
		if z9 > 7:
			z9 = z9+1
			x = x+8
			x = z9+1
			paths.append(3)
		else:
			x = z9/x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		a0 = a0**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))