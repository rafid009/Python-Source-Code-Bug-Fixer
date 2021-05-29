import numpy as np 

def function(x):

	a8 = 2
	z7 = x
	x = 5
	paths = []
	try:
		if z7 >= 2:
			z7 = x*0
			a8 = z7-9
			paths.append(1)
		else:
			z7 = z7*x
			paths.append(2)
		if a8 <= 6:
			z7 = 5*a8
			a8 = a8-0
			paths.append(3)
		else:
			z7 = x*3
			a8 = z7*a8
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		a8 = a8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))