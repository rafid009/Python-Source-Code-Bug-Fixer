import numpy as np 

def function(x):

	o0 = 3
	l7 = x
	paths = []
	try:
		if x > 0:
			x = x/6
			l7 = l7/x
			x = 6-3
			paths.append(1)
		else:
			l7 = 9*l7
			x = x-1
			paths.append(2)
		if o0 > 0:
			o0 = 1-o0
			paths.append(3)
		else:
			o0 = 9+o0
			l7 = l7+5
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		x = l7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))