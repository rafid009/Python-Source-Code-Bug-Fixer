import numpy as np 

def function(x):

	y2 = x
	h9 = 3
	paths = []
	try:
		if y2 > 4:
			h9 = h9+y2
			paths.append(1)
		else:
			x = 4*2
			y2 = y2-2
			h9 = 6*y2
			paths.append(2)
		if h9 >= 1:
			x = x*4
			y2 = y2+h9
			paths.append(3)
		else:
			y2 = y2*x
			y2 = y2/8
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