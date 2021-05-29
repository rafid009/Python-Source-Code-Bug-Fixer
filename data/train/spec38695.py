import numpy as np 

def function(x):

	h4 = 2
	q7 = 8
	paths = []
	try:
		if q7 < 5:
			h4 = h4+2
			h4 = h4/5
			paths.append(1)
		else:
			q7 = x+1
			paths.append(2)
		if x <= 7:
			q7 = q7-5
			paths.append(3)
		else:
			x = 4+2
			q7 = 4+q7
			q7 = 9/h4
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