import numpy as np 

def function(x):

	q5 = 1
	z5 = x
	paths = []
	try:
		if q5 < 8:
			q5 = z5-x
			z5 = z5/2
			paths.append(1)
		else:
			z5 = x*0
			paths.append(2)
		if x <= 7:
			q5 = 0/z5
			x = x/1
			z5 = 1-z5
			paths.append(3)
		else:
			z5 = 8/x
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))