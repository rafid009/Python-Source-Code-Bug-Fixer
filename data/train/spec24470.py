import numpy as np 

def function(x):

	q5 = x
	z0 = 8
	paths = []
	try:
		if x > 7:
			q5 = x-z0
			paths.append(1)
		else:
			x = 8/x
			x = z0/7
			x = x-3
			paths.append(2)
		if z0 > 4:
			q5 = q5+3
			paths.append(3)
		else:
			x = 4+x
			q5 = q5*8
			z0 = x-0
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		x = q5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))