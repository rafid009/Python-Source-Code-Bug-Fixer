import numpy as np 

def function(x):

	u7 = 8
	w1 = 5
	paths = []
	try:
		if u7 <= 2:
			x = 0+x
			u7 = x+4
			paths.append(1)
		else:
			w1 = 6/x
			paths.append(2)
		if w1 <= 3:
			u7 = u7/u7
			w1 = w1-4
			paths.append(3)
		else:
			u7 = 1/u7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))