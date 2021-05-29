import numpy as np 

def function(x):

	l9 = 5
	h9 = x
	paths = []
	try:
		if h9 < 1:
			h9 = 9+h9
			paths.append(1)
		else:
			h9 = 0-7
			paths.append(2)
		if x < 3:
			l9 = h9/9
			paths.append(3)
		else:
			x = x*1
			l9 = l9*6
			l9 = 6-6
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		x = h9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))