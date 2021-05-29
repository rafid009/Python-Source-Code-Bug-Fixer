import numpy as np 

def function(x):

	l4 = 8
	v9 = 5
	paths = []
	try:
		if l4 >= 3:
			l4 = l4*x
			paths.append(1)
		else:
			x = 7-5
			x = 2+x
			paths.append(2)
		if l4 >= 2:
			v9 = l4-v9
			v9 = 4+v9
			paths.append(3)
		else:
			v9 = 6/v9
			x = 3*x
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