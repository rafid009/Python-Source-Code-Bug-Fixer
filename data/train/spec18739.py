import numpy as np 

def function(x):

	q6 = x
	z7 = x
	paths = []
	try:
		if q6 <= 3:
			z7 = z7/2
			z7 = 7/8
			z7 = x*z7
			paths.append(1)
		else:
			q6 = 3-q6
			x = x/8
			paths.append(2)
		if q6 > 8:
			x = x/5
			x = x*7
			x = 5+x
			paths.append(3)
		else:
			x = 5-x
			q6 = q6-1
			x = x/z7
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		z7 = z7**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))