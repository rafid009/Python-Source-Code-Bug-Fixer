import numpy as np 

def function(x):

	y7 = x
	l4 = 5
	paths = []
	try:
		if l4 < 3:
			l4 = l4+7
			y7 = y7+x
			x = x/7
			paths.append(1)
		else:
			x = x/4
			x = y7-y7
			x = x-2
			paths.append(2)
		if x >= 0:
			x = x+9
			y7 = x*y7
			y7 = y7/y7
			paths.append(3)
		else:
			l4 = 6+l4
			l4 = 5*l4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))