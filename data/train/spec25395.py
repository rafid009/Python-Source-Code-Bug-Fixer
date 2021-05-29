import numpy as np 

def function(x):

	o7 = x
	l0 = 2
	paths = []
	try:
		if l0 > 8:
			o7 = 8*o7
			x = 6/x
			paths.append(1)
		else:
			x = x*3
			o7 = 6/o7
			x = 2-x
			paths.append(2)
		if l0 > 1:
			l0 = 8+l0
			paths.append(3)
		else:
			x = o7+7
			l0 = l0-l0
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		x = o7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))