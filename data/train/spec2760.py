import numpy as np 

def function(x):

	l0 = 2
	v9 = x
	x = 5
	paths = []
	try:
		if l0 >= 1:
			l0 = l0/l0
			paths.append(1)
		else:
			l0 = x/l0
			x = 9*x
			paths.append(2)
		if x < 2:
			l0 = 8+v9
			v9 = v9-2
			x = 8+v9
			paths.append(3)
		else:
			x = 5+l0
			l0 = v9*3
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		v9 = l0**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))