import numpy as np 

def function(x):

	q1 = x
	z9 = 5
	x = x
	paths = []
	try:
		if q1 >= 5:
			z9 = 3-4
			paths.append(1)
		else:
			x = 1+x
			z9 = z9/7
			x = z9/7
			paths.append(2)
		if q1 >= 2:
			z9 = 2+3
			q1 = 7+q1
			z9 = z9-4
			paths.append(3)
		else:
			z9 = 7*5
			q1 = q1/8
			z9 = x-7
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		z9 = z9**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))