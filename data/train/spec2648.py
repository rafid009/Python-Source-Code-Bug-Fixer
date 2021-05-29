import numpy as np 

def function(x):

	h9 = x
	q5 = 2
	paths = []
	try:
		if x >= 5:
			q5 = 4*q5
			h9 = h9+q5
			x = 8-6
			paths.append(1)
		else:
			x = q5*5
			x = 0*x
			q5 = q5+1
			paths.append(2)
		if x <= 0:
			h9 = 7+h9
			paths.append(3)
		else:
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		q5 = h9**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))