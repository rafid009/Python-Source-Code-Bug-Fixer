import numpy as np 

def function(x):

	a2 = 1
	z7 = x
	paths = []
	try:
		if z7 > 0:
			x = x+6
			z7 = 4*x
			paths.append(1)
		else:
			x = 1+x
			paths.append(2)
		if a2 <= 5:
			x = x+7
			a2 = a2*8
			x = 5+x
			paths.append(3)
		else:
			z7 = z7+a2
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		a2 = z7**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))