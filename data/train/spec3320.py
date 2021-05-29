import numpy as np 

def function(x):

	q5 = x
	z1 = 8
	paths = []
	try:
		if z1 > 2:
			x = 7/1
			q5 = 7*q5
			q5 = 4-9
			paths.append(1)
		else:
			q5 = q5*2
			x = 9*z1
			z1 = 6-8
			paths.append(2)
		if x < 2:
			x = z1-3
			paths.append(3)
		else:
			q5 = q5-2
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		q5 = q5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))