import numpy as np 

def function(x):

	z6 = 5
	q4 = x
	paths = []
	try:
		if x < 8:
			z6 = 1-4
			paths.append(1)
		else:
			q4 = 9+q4
			paths.append(2)
		if x <= 5:
			q4 = q4+2
			q4 = z6+1
			z6 = z6/5
			paths.append(3)
		else:
			q4 = q4/q4
			x = x-6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		z6 = z6**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))