import numpy as np 

def function(x):

	l9 = 3
	o4 = x
	x = 5
	paths = []
	try:
		if o4 > 9:
			x = l9/6
			paths.append(1)
		else:
			x = 3/o4
			l9 = 4+2
			l9 = l9+l9
			paths.append(2)
		if x >= 0:
			l9 = 7-l9
			o4 = 3+o4
			paths.append(3)
		else:
			o4 = 3-l9
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		x = l9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))