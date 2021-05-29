import numpy as np 

def function(x):

	h7 = x
	q8 = x
	paths = []
	try:
		if q8 < 3:
			x = 3+3
			h7 = h7+4
			x = 1*6
			paths.append(1)
		else:
			x = x*8
			x = 1-x
			paths.append(2)
		if x < 7:
			q8 = 8+q8
			q8 = q8/3
			q8 = h7-q8
			paths.append(3)
		else:
			x = 9*x
			x = x+4
			x = x*h7
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x = q8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))