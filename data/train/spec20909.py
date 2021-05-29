import numpy as np 

def function(x):

	l6 = 8
	y3 = 2
	paths = []
	try:
		if x > 7:
			y3 = y3/x
			x = 1/l6
			y3 = y3*x
			paths.append(1)
		else:
			y3 = 8/6
			y3 = l6/y3
			paths.append(2)
		if l6 <= 3:
			l6 = 1*1
			y3 = 1+y3
			paths.append(3)
		else:
			l6 = l6-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))