import numpy as np 

def function(x):

	l8 = x
	q4 = 7
	paths = []
	try:
		if x > 5:
			l8 = 7+l8
			q4 = 6-4
			paths.append(1)
		else:
			q4 = q4*x
			l8 = l8*1
			q4 = q4/l8
			paths.append(2)
		if q4 <= 8:
			x = x/q4
			x = x/8
			paths.append(3)
		else:
			l8 = q4-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))