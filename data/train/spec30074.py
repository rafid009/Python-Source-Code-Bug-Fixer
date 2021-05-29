import numpy as np 

def function(x):

	w6 = x
	y7 = x
	paths = []
	try:
		if y7 > 1:
			x = x+7
			x = w6+y7
			x = w6*x
			paths.append(1)
		else:
			x = x+9
			x = 6/5
			w6 = 0-5
			paths.append(2)
		if x >= 1:
			x = x/2
			w6 = w6-5
			w6 = w6+2
			paths.append(3)
		else:
			y7 = y7-6
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))