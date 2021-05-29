import numpy as np 

def function(x):

	x1 = 6
	q5 = 0
	paths = []
	try:
		if x <= 6:
			q5 = q5-q5
			paths.append(1)
		else:
			x1 = 3+5
			paths.append(2)
		if x <= 7:
			q5 = x/9
			q5 = q5*8
			paths.append(3)
		else:
			q5 = q5-q5
			q5 = q5*q5
			x1 = x*x1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))