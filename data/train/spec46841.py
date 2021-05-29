import numpy as np 

def function(x):

	q7 = 6
	r9 = x
	paths = []
	try:
		if r9 > 2:
			x = x+5
			x = 6/2
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if x >= 0:
			x = r9*r9
			paths.append(3)
		else:
			q7 = q7-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))