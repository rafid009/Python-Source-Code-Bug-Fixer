import numpy as np 

def function(x):

	d5 = x
	k7 = 7
	paths = []
	try:
		if k7 >= 7:
			k7 = k7+8
			x = k7+k7
			paths.append(1)
		else:
			k7 = 5+k7
			x = x*x
			paths.append(2)
		if k7 >= 0:
			d5 = d5*6
			k7 = k7+8
			paths.append(3)
		else:
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))