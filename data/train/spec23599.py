import numpy as np 

def function(x):

	q9 = x
	h4 = 7
	paths = []
	try:
		if x < 4:
			h4 = 0+h4
			q9 = x*x
			x = 9+6
			paths.append(1)
		else:
			h4 = h4*q9
			x = x*6
			x = 7-q9
			paths.append(2)
		if h4 > 3:
			h4 = x*h4
			h4 = q9/h4
			paths.append(3)
		else:
			x = x*h4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))