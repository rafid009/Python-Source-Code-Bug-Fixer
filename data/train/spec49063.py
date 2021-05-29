import numpy as np 

def function(x):

	y2 = 8
	h9 = x
	paths = []
	try:
		if h9 > 5:
			y2 = 2-x
			paths.append(1)
		else:
			x = 2*x
			paths.append(2)
		if y2 >= 3:
			y2 = y2-1
			x = x-3
			y2 = 6-7
			paths.append(3)
		else:
			y2 = x+y2
			x = h9-2
			y2 = x*9
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		h9 = h9**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))