import numpy as np 

def function(x):

	h8 = 1
	q5 = 5
	paths = []
	try:
		if x >= 7:
			x = x*7
			x = x*8
			x = 4+q5
			paths.append(1)
		else:
			q5 = 3/q5
			paths.append(2)
		if x < 3:
			h8 = 6*x
			h8 = h8-9
			h8 = 0-h8
			paths.append(3)
		else:
			x = 1-0
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		h8 = h8**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))