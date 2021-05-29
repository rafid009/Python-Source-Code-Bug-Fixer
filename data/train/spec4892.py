import numpy as np 

def function(x):

	y2 = 7
	w6 = 7
	paths = []
	try:
		if x >= 5:
			x = x*5
			y2 = 7/y2
			paths.append(1)
		else:
			w6 = w6/8
			x = 0-x
			paths.append(2)
		if w6 > 6:
			x = x*3
			paths.append(3)
		else:
			w6 = x*1
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		x = w6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))