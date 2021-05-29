import numpy as np 

def function(x):

	y4 = 8
	w4 = 5
	paths = []
	try:
		if w4 <= 8:
			y4 = 8*y4
			y4 = y4+1
			paths.append(1)
		else:
			y4 = w4+x
			paths.append(2)
		if w4 < 6:
			y4 = w4-y4
			paths.append(3)
		else:
			y4 = 5+y4
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