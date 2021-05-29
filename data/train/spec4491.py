import numpy as np 

def function(x):

	a6 = x
	q7 = x
	paths = []
	try:
		if a6 <= 7:
			q7 = q7/2
			q7 = 8*q7
			paths.append(1)
		else:
			a6 = x/8
			x = x/8
			paths.append(2)
		if a6 >= 4:
			q7 = q7*q7
			paths.append(3)
		else:
			a6 = 5*5
			x = 1*x
			q7 = q7*4
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