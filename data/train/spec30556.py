import numpy as np 

def function(x):

	w7 = x
	u2 = 1
	paths = []
	try:
		if u2 < 9:
			w7 = 2*w7
			paths.append(1)
		else:
			w7 = 5*w7
			paths.append(2)
		if w7 < 8:
			w7 = w7/4
			paths.append(3)
		else:
			u2 = w7+u2
			w7 = 5-8
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		u2 = w7**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))