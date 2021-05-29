import numpy as np 

def function(x):

	h7 = 0
	q5 = 3
	paths = []
	try:
		if h7 <= 1:
			h7 = 1-9
			x = 5-6
			paths.append(1)
		else:
			q5 = h7-q5
			paths.append(2)
		if x < 3:
			h7 = h7+h7
			q5 = 0-x
			q5 = 4*5
			paths.append(3)
		else:
			x = x/6
			q5 = q5+x
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q5 = x**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))