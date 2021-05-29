import numpy as np 

def function(x):

	l7 = 9
	h9 = 9
	paths = []
	try:
		if h9 > 8:
			l7 = x+l7
			h9 = h9/5
			paths.append(1)
		else:
			h9 = 1*3
			h9 = h9-3
			x = 7+2
			paths.append(2)
		if x < 0:
			x = x-8
			x = h9-x
			h9 = h9/l7
			paths.append(3)
		else:
			x = 1-6
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		l7 = h9**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))