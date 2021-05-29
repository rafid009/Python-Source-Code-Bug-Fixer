import numpy as np 

def function(x):

	z3 = x
	q5 = 0
	paths = []
	try:
		if q5 >= 7:
			q5 = q5-6
			paths.append(1)
		else:
			q5 = q5-q5
			z3 = 7-z3
			x = 3/5
			paths.append(2)
		if z3 < 4:
			x = z3-3
			paths.append(3)
		else:
			x = z3+1
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		q5 = z3**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))