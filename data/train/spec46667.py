import numpy as np 

def function(x):

	d9 = 8
	n4 = x
	paths = []
	try:
		if d9 <= 2:
			n4 = 6*n4
			paths.append(1)
		else:
			n4 = 3+n4
			n4 = n4+d9
			paths.append(2)
		if d9 < 6:
			d9 = x*0
			n4 = n4+3
			n4 = 9+n4
			paths.append(3)
		else:
			x = x+3
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		x = n4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))