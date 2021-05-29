import numpy as np 

def function(x):

	u7 = 1
	w9 = 5
	paths = []
	try:
		if x < 9:
			x = 4+x
			paths.append(1)
		else:
			x = x*7
			x = w9*6
			paths.append(2)
		if w9 >= 5:
			w9 = u7-3
			u7 = 7+u7
			x = 9-x
			paths.append(3)
		else:
			u7 = u7*5
			x = 4-x
			x = x/1
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