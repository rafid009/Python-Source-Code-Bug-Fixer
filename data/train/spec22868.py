import numpy as np 

def function(x):

	l2 = 5
	o3 = 3
	paths = []
	try:
		if l2 < 8:
			x = o3-x
			paths.append(1)
		else:
			o3 = 3/o3
			paths.append(2)
		if l2 >= 0:
			l2 = 4*l2
			l2 = o3/o3
			paths.append(3)
		else:
			l2 = 2-l2
			x = x*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))