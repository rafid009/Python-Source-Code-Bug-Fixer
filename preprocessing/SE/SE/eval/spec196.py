import numpy as np 

def function(x):

	w6 = 9
	j8 = 2
	paths = []
	try:
		if w6 < 2:
			j8 = x+7
			j8 = j8/j8
			paths.append(1)
		else:
			w6 = 7/w6
			paths.append(2)
		if w6 <= 0:
			w6 = w6-7
			paths.append(3)
		else:
			w6 = 6*7
			j8 = 1/j8
			j8 = 7*3
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