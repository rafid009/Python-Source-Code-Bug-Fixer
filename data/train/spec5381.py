import numpy as np 

def function(x):

	y6 = x
	w1 = 9
	paths = []
	try:
		if w1 >= 9:
			y6 = 1-y6
			w1 = w1/3
			paths.append(1)
		else:
			w1 = 7/w1
			x = 8/8
			paths.append(2)
		if y6 > 1:
			x = x*7
			w1 = 5-9
			paths.append(3)
		else:
			x = 9/x
			x = x-x
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		y6 = w1**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))