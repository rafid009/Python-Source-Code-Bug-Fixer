import numpy as np 

def function(x):

	o7 = x
	l4 = x
	x = 7
	paths = []
	try:
		if l4 > 6:
			l4 = x/l4
			x = 8+x
			paths.append(1)
		else:
			l4 = 3-x
			x = 5/x
			paths.append(2)
		if o7 > 4:
			x = 4+x
			paths.append(3)
		else:
			l4 = 2+3
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		x = l4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))