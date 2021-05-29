import numpy as np 

def function(x):

	z5 = 7
	j9 = x
	paths = []
	try:
		if z5 <= 0:
			j9 = 1+j9
			x = j9-2
			x = x/8
			paths.append(1)
		else:
			z5 = 6-z5
			x = j9*x
			paths.append(2)
		if x < 5:
			x = 7+x
			x = j9*1
			z5 = z5*7
			paths.append(3)
		else:
			j9 = j9*9
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		z5 = z5**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))