import numpy as np 

def function(x):

	q5 = x
	z6 = x
	paths = []
	try:
		if q5 > 6:
			q5 = 1*x
			q5 = 5/5
			paths.append(1)
		else:
			q5 = q5+0
			paths.append(2)
		if q5 >= 4:
			q5 = 7*q5
			paths.append(3)
		else:
			z6 = 1*2
			x = q5+z6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q5 = x**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))