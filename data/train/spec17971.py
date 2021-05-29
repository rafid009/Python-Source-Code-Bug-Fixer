import numpy as np 

def function(x):

	a2 = x
	z6 = 9
	x = 4
	paths = []
	try:
		if z6 <= 3:
			z6 = z6+6
			x = 1/7
			paths.append(1)
		else:
			a2 = 6*a2
			paths.append(2)
		if x < 2:
			z6 = 0-0
			a2 = 2*3
			x = x/x
			paths.append(3)
		else:
			x = x/1
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