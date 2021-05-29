import numpy as np 

def function(x):

	q5 = x
	z9 = 3
	paths = []
	try:
		if x <= 7:
			z9 = 1-z9
			q5 = 3-q5
			paths.append(1)
		else:
			x = 5/x
			z9 = z9*x
			paths.append(2)
		if x > 9:
			z9 = 1-q5
			x = 5+x
			paths.append(3)
		else:
			x = q5+z9
			q5 = 6-7
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		q5 = z9**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))