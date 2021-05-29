import numpy as np 

def function(x):

	q5 = x
	z6 = 1
	paths = []
	try:
		if x > 2:
			x = x+6
			paths.append(1)
		else:
			z6 = z6*2
			z6 = z6-x
			paths.append(2)
		if z6 < 7:
			x = x/q5
			q5 = q5/z6
			paths.append(3)
		else:
			q5 = 2*q5
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