import numpy as np 

def function(x):

	k7 = x
	y4 = 1
	paths = []
	try:
		if x <= 1:
			x = y4-x
			x = 9/x
			paths.append(1)
		else:
			y4 = y4+0
			paths.append(2)
		if k7 <= 5:
			x = 6/4
			paths.append(3)
		else:
			x = x/4
			y4 = y4*3
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		y4 = k7**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))