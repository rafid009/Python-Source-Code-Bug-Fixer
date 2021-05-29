import numpy as np 

def function(x):

	q5 = x
	h0 = x
	paths = []
	try:
		if q5 <= 3:
			q5 = 1*q5
			paths.append(1)
		else:
			h0 = x/5
			q5 = h0+2
			paths.append(2)
		if q5 <= 4:
			q5 = q5*9
			paths.append(3)
		else:
			h0 = h0*0
			h0 = h0/4
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