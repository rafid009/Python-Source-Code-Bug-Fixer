import numpy as np 

def function(x):

	y0 = x
	h4 = x
	paths = []
	try:
		if x <= 4:
			y0 = y0/h4
			x = 3+x
			x = 6+x
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if x < 9:
			x = x+0
			paths.append(3)
		else:
			y0 = 8/y0
			x = x-8
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		h4 = h4**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))