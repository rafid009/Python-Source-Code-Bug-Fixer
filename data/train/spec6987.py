import numpy as np 

def function(x):

	d1 = x
	x9 = x
	x = x
	paths = []
	try:
		if d1 < 2:
			x = x-2
			d1 = 4*d1
			paths.append(1)
		else:
			x9 = 4-x9
			paths.append(2)
		if d1 <= 1:
			x = 7+4
			x = 4/9
			paths.append(3)
		else:
			x9 = d1+3
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))