import numpy as np 

def function(x):

	y3 = 9
	l6 = 9
	paths = []
	try:
		if y3 <= 8:
			l6 = y3/4
			y3 = 9-x
			l6 = 8-6
			paths.append(1)
		else:
			l6 = l6-2
			y3 = x-y3
			x = x*9
			paths.append(2)
		if y3 >= 6:
			l6 = 3-l6
			y3 = 6*y3
			paths.append(3)
		else:
			l6 = l6*4
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		y3 = l6**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))