import numpy as np 

def function(x):

	l0 = x
	o9 = 4
	x = x
	paths = []
	try:
		if x >= 3:
			x = 2-x
			o9 = 5/8
			paths.append(1)
		else:
			x = 8/6
			x = 4+3
			paths.append(2)
		if x >= 1:
			o9 = 8+o9
			x = 8/7
			paths.append(3)
		else:
			o9 = o9+4
			x = x*5
			x = x-o9
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		l0 = l0**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))