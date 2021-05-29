import numpy as np 

def function(x):

	t7 = x
	y2 = x
	paths = []
	try:
		if t7 < 1:
			x = 5*x
			y2 = 1+x
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if x > 9:
			x = x-3
			paths.append(3)
		else:
			y2 = y2/6
			y2 = 7/y2
			y2 = 2-y2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))