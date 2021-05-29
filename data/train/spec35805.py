import numpy as np 

def function(x):

	q4 = x
	z5 = 0
	paths = []
	try:
		if z5 > 5:
			q4 = 5+x
			z5 = 3*z5
			paths.append(1)
		else:
			x = 4/4
			x = x*1
			q4 = q4/4
			paths.append(2)
		if q4 < 8:
			z5 = z5+7
			q4 = q4/2
			paths.append(3)
		else:
			x = 2-9
			q4 = 3/x
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		x = q4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))