import numpy as np 

def function(x):

	z2 = x
	a4 = 5
	paths = []
	try:
		if a4 > 3:
			a4 = x-4
			x = x+6
			z2 = 7*x
			paths.append(1)
		else:
			x = z2/x
			z2 = z2+z2
			paths.append(2)
		if a4 <= 8:
			x = x+x
			x = x*5
			paths.append(3)
		else:
			x = x/5
			z2 = 0/6
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		a4 = a4**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))