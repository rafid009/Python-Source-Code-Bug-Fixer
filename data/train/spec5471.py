import numpy as np 

def function(x):

	u2 = x
	d7 = x
	paths = []
	try:
		if d7 <= 6:
			x = 7*x
			x = x-2
			u2 = 2*4
			paths.append(1)
		else:
			u2 = u2*d7
			d7 = 5/d7
			paths.append(2)
		if d7 > 3:
			u2 = x-u2
			x = 2*x
			paths.append(3)
		else:
			u2 = 9-0
			u2 = 8-x
			d7 = u2+d7
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		d7 = d7**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))