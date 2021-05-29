import numpy as np 

def function(x):

	n0 = 9
	u4 = x
	paths = []
	try:
		if x <= 0:
			n0 = 7-u4
			paths.append(1)
		else:
			x = 5+x
			x = x+x
			paths.append(2)
		if n0 > 0:
			x = u4*5
			n0 = 4*u4
			paths.append(3)
		else:
			n0 = u4/5
			x = x/3
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))