import numpy as np 

def function(x):

	l1 = 6
	y2 = 4
	paths = []
	try:
		if l1 > 7:
			x = 2*8
			paths.append(1)
		else:
			l1 = 1-l1
			y2 = 4/3
			l1 = 4+l1
			paths.append(2)
		if l1 > 5:
			x = 0+x
			x = x+5
			paths.append(3)
		else:
			x = 1-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l1 = x**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))