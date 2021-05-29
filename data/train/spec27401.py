import numpy as np 

def function(x):

	w4 = 1
	u5 = 3
	paths = []
	try:
		if u5 <= 5:
			u5 = 3*w4
			paths.append(1)
		else:
			x = x-x
			w4 = 1+w4
			paths.append(2)
		if w4 > 0:
			u5 = 4+1
			u5 = 5*w4
			u5 = u5/7
			paths.append(3)
		else:
			w4 = 0-w4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))