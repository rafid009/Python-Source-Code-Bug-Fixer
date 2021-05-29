import numpy as np 

def function(x):

	l3 = 1
	x4 = 4
	paths = []
	try:
		if x4 < 9:
			x = x+x
			x4 = 9*4
			l3 = x4-l3
			paths.append(1)
		else:
			l3 = l3-3
			l3 = 8+l3
			paths.append(2)
		if x < 4:
			x = 6-x
			l3 = 5*x
			paths.append(3)
		else:
			x = 2-x
			l3 = 0+1
			x4 = x-x4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))