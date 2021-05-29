import numpy as np 

def function(x):

	w1 = 8
	u7 = 5
	x = x
	paths = []
	try:
		if u7 <= 3:
			x = 6-x
			x = x-w1
			w1 = w1+6
			paths.append(1)
		else:
			u7 = u7/2
			u7 = 8/x
			paths.append(2)
		if w1 < 1:
			u7 = u7*6
			paths.append(3)
		else:
			x = x-2
			w1 = 8/3
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		w1 = u7**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))