import numpy as np 

def function(x):

	q5 = x
	h9 = 1
	paths = []
	try:
		if x > 7:
			x = 3-7
			q5 = 8*q5
			paths.append(1)
		else:
			h9 = q5/h9
			h9 = q5*h9
			paths.append(2)
		if q5 < 8:
			h9 = x/h9
			q5 = q5*9
			paths.append(3)
		else:
			q5 = 3*q5
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