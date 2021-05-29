import numpy as np 

def function(x):

	o9 = 4
	l8 = x
	paths = []
	try:
		if x > 3:
			l8 = o9*l8
			paths.append(1)
		else:
			x = o9-o9
			paths.append(2)
		if o9 >= 2:
			x = l8+9
			l8 = 1/l8
			o9 = 8-o9
			paths.append(3)
		else:
			o9 = o9-5
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