import numpy as np 

def function(x):

	z6 = x
	q5 = 6
	paths = []
	try:
		if q5 < 7:
			x = x-3
			paths.append(1)
		else:
			z6 = x/9
			x = 4/q5
			z6 = 4/5
			paths.append(2)
		if q5 < 8:
			x = 1/q5
			x = 6*2
			paths.append(3)
		else:
			z6 = q5*1
			z6 = 3*z6
			z6 = z6/5
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))