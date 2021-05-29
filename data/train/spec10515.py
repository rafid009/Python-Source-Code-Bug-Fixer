import numpy as np 

def function(x):

	h6 = x
	q6 = x
	paths = []
	try:
		if h6 >= 9:
			h6 = q6+1
			paths.append(1)
		else:
			x = x/3
			q6 = 2-q6
			q6 = q6/4
			paths.append(2)
		if x > 7:
			x = x/9
			h6 = 9+h6
			paths.append(3)
		else:
			q6 = q6+x
			q6 = x*q6
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		h6 = q6**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))