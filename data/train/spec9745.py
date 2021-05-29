import numpy as np 

def function(x):

	r9 = 3
	l8 = x
	paths = []
	try:
		if l8 <= 2:
			x = x*6
			paths.append(1)
		else:
			l8 = x+l8
			paths.append(2)
		if x <= 9:
			l8 = r9-l8
			paths.append(3)
		else:
			l8 = 9-l8
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		r9 = l8**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))