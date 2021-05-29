import numpy as np 

def function(x):

	u7 = 4
	w9 = 7
	paths = []
	try:
		if x <= 1:
			u7 = 0*u7
			w9 = 3+w9
			paths.append(1)
		else:
			x = x/2
			w9 = w9*u7
			x = 1-x
			paths.append(2)
		if w9 > 0:
			u7 = u7*7
			paths.append(3)
		else:
			x = 0+u7
			u7 = u7*w9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))