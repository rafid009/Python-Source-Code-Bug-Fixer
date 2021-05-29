import numpy as np 

def function(x):

	o0 = 8
	l0 = 8
	paths = []
	try:
		if x >= 6:
			l0 = 0-7
			paths.append(1)
		else:
			x = x*o0
			x = 9+x
			paths.append(2)
		if x <= 0:
			o0 = 2/o0
			paths.append(3)
		else:
			x = 9/x
			l0 = 9*l0
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		o0 = l0**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))