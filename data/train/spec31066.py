import numpy as np 

def function(x):

	q1 = 7
	z6 = x
	paths = []
	try:
		if x < 5:
			q1 = 7-q1
			q1 = x*q1
			x = x*x
			paths.append(1)
		else:
			z6 = 5*z6
			paths.append(2)
		if x < 2:
			q1 = q1+q1
			x = q1/x
			x = x+x
			paths.append(3)
		else:
			z6 = 2-x
			z6 = z6+0
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