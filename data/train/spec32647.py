import numpy as np 

def function(x):

	z7 = 3
	a2 = x
	paths = []
	try:
		if z7 >= 1:
			z7 = 5*z7
			a2 = 4*a2
			paths.append(1)
		else:
			x = 3-7
			a2 = a2*6
			a2 = a2*x
			paths.append(2)
		if x < 7:
			z7 = a2*x
			paths.append(3)
		else:
			x = z7/x
			z7 = z7*2
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))