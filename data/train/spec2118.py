import numpy as np 

def function(x):

	h9 = x
	y2 = 9
	paths = []
	try:
		if x <= 2:
			y2 = y2-1
			y2 = 2/6
			x = 1/3
			paths.append(1)
		else:
			y2 = 2+y2
			h9 = 8-h9
			paths.append(2)
		if h9 <= 3:
			h9 = 5/4
			x = x+x
			x = x+0
			paths.append(3)
		else:
			y2 = x-8
			x = h9/1
			x = x-x
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		x = y2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))