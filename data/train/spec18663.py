import numpy as np 

def function(x):

	l9 = x
	y1 = 3
	paths = []
	try:
		if y1 < 5:
			y1 = x/5
			l9 = x*9
			paths.append(1)
		else:
			l9 = 4/x
			l9 = y1+3
			paths.append(2)
		if l9 > 1:
			y1 = 8-y1
			y1 = 6/y1
			y1 = x-8
			paths.append(3)
		else:
			l9 = y1*6
			y1 = y1+0
			l9 = 0-l9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y1 = x**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))