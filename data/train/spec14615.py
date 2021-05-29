import numpy as np 

def function(x):

	x7 = 2
	l1 = x
	paths = []
	try:
		if x <= 3:
			x = x+x
			l1 = x+5
			x = l1*3
			paths.append(1)
		else:
			l1 = 3+l1
			x = 8/x
			x7 = 1-x7
			paths.append(2)
		if x < 4:
			l1 = 1-l1
			paths.append(3)
		else:
			x7 = x7*2
			x = 3+6
			x7 = 0*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))