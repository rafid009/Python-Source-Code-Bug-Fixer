import numpy as np 

def function(x):

	t0 = x
	l8 = 6
	paths = []
	try:
		if x >= 0:
			l8 = l8*t0
			x = x*4
			l8 = x/t0
			paths.append(1)
		else:
			x = x-x
			l8 = 7+7
			l8 = l8-2
			paths.append(2)
		if x >= 4:
			x = l8-x
			x = 4/2
			l8 = l8/t0
			paths.append(3)
		else:
			l8 = l8+2
			x = x*l8
			l8 = l8-7
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		l8 = l8**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))