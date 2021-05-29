import numpy as np 

def function(x):

	e6 = x
	z1 = 7
	paths = []
	try:
		if z1 <= 6:
			e6 = e6/6
			e6 = z1-e6
			x = x*0
			paths.append(1)
		else:
			z1 = z1+3
			e6 = 9/e6
			paths.append(2)
		if x > 6:
			z1 = z1+5
			e6 = 9+x
			paths.append(3)
		else:
			x = x-z1
			z1 = 5-9
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e6 = e6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))