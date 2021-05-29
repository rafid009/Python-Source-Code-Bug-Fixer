import numpy as np 

def function(x):

	h6 = x
	y7 = 1
	paths = []
	try:
		if h6 > 2:
			y7 = 7*h6
			x = 6-x
			x = x+x
			paths.append(1)
		else:
			h6 = h6/6
			y7 = y7+5
			x = x/3
			paths.append(2)
		if y7 <= 1:
			h6 = 9/x
			y7 = x*y7
			paths.append(3)
		else:
			x = 2+x
			x = x-x
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		y7 = h6**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))