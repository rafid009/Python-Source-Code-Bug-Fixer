import numpy as np 

def function(x):

	z3 = 0
	q7 = 8
	paths = []
	try:
		if q7 > 9:
			z3 = z3*0
			z3 = 3*8
			q7 = q7/z3
			paths.append(1)
		else:
			z3 = z3+5
			q7 = x*q7
			z3 = 0+x
			paths.append(2)
		if x > 7:
			q7 = q7-q7
			paths.append(3)
		else:
			q7 = q7-x
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		x = q7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))