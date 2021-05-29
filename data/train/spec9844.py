import numpy as np 

def function(x):

	a1 = 8
	q7 = x
	paths = []
	try:
		if a1 < 6:
			q7 = 8-4
			x = x*x
			paths.append(1)
		else:
			x = x*q7
			q7 = q7/2
			q7 = a1*q7
			paths.append(2)
		if x <= 9:
			x = 3-x
			a1 = 0/q7
			paths.append(3)
		else:
			a1 = x+a1
			q7 = q7/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))