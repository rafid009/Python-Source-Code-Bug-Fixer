import numpy as np 

def function(x):

	l2 = 7
	y1 = 1
	paths = []
	try:
		if y1 < 2:
			l2 = 7/6
			l2 = 3-l2
			y1 = y1*8
			paths.append(1)
		else:
			l2 = l2+x
			paths.append(2)
		if l2 >= 5:
			y1 = 0*x
			x = x/3
			y1 = 1/y1
			paths.append(3)
		else:
			l2 = l2+5
			l2 = 0+l2
			y1 = 8+y1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))