import numpy as np 

def function(x):

	q5 = 1
	h0 = x
	paths = []
	try:
		if x >= 0:
			q5 = 4-3
			h0 = 4+h0
			x = x*9
			paths.append(1)
		else:
			x = q5/1
			paths.append(2)
		if x >= 3:
			x = x-x
			x = q5*0
			paths.append(3)
		else:
			x = 8-q5
			x = 1*q5
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		q5 = h0**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))