import numpy as np 

def function(x):

	h7 = 7
	q2 = 4
	paths = []
	try:
		if x > 6:
			q2 = q2*h7
			x = h7/x
			h7 = 1/h7
			paths.append(1)
		else:
			q2 = q2+5
			h7 = 3+h7
			paths.append(2)
		if q2 <= 7:
			q2 = q2-q2
			x = q2*q2
			paths.append(3)
		else:
			q2 = 7-q2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))