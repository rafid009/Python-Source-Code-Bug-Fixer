import numpy as np 

def function(x):

	y1 = 0
	l9 = x
	x = x
	paths = []
	try:
		if x <= 2:
			x = x/4
			paths.append(1)
		else:
			x = x*l9
			paths.append(2)
		if l9 <= 4:
			l9 = l9+5
			x = 5-x
			y1 = y1-8
			paths.append(3)
		else:
			l9 = x*l9
			l9 = 5/l9
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