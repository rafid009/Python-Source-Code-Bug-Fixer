import numpy as np 

def function(x):

	h0 = 6
	q5 = x
	paths = []
	try:
		if x >= 7:
			q5 = q5*3
			paths.append(1)
		else:
			h0 = h0+1
			x = 2/q5
			q5 = 2/x
			paths.append(2)
		if h0 >= 5:
			x = x/2
			h0 = h0*1
			h0 = 4+3
			paths.append(3)
		else:
			x = 5*x
			h0 = 3+h0
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		q5 = q5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))