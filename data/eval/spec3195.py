import numpy as np 

def function(x):

	q3 = x
	z1 = 9
	paths = []
	try:
		if z1 <= 3:
			z1 = q3/5
			paths.append(1)
		else:
			q3 = q3/8
			x = x-q3
			z1 = x+q3
			paths.append(2)
		if z1 <= 2:
			q3 = q3/1
			paths.append(3)
		else:
			q3 = q3*x
			x = x*9
			x = 2+z1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q3 = x**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))