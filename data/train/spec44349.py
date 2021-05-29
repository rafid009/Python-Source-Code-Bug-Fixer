import numpy as np 

def function(x):

	q7 = x
	t8 = 8
	paths = []
	try:
		if x < 5:
			x = q7+8
			paths.append(1)
		else:
			q7 = q7*x
			paths.append(2)
		if q7 >= 1:
			q7 = 0*q7
			q7 = q7*t8
			paths.append(3)
		else:
			q7 = 1-3
			x = x*2
			x = x/8
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