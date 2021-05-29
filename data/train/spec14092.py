import numpy as np 

def function(x):

	z9 = x
	q9 = 4
	paths = []
	try:
		if x < 5:
			z9 = z9*q9
			paths.append(1)
		else:
			q9 = q9+9
			paths.append(2)
		if q9 < 8:
			x = x/9
			z9 = z9*7
			paths.append(3)
		else:
			z9 = z9/3
			x = 7/6
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		q9 = z9**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))