import numpy as np 

def function(x):

	x6 = x
	w1 = 9
	paths = []
	try:
		if w1 < 3:
			w1 = w1-4
			paths.append(1)
		else:
			x6 = 3-x6
			paths.append(2)
		if x <= 3:
			w1 = w1*3
			paths.append(3)
		else:
			x = x6+3
			w1 = 6-x6
			x6 = w1-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))