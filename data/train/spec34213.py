import numpy as np 

def function(x):

	l8 = 7
	r9 = 5
	paths = []
	try:
		if r9 < 4:
			l8 = l8*3
			l8 = l8-2
			paths.append(1)
		else:
			x = 4*5
			l8 = l8-9
			x = 0+2
			paths.append(2)
		if r9 >= 3:
			r9 = 3-3
			paths.append(3)
		else:
			l8 = l8+7
			x = x*8
			x = 6*x
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