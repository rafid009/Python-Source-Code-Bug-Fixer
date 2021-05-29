import numpy as np 

def function(x):

	v7 = x
	d4 = 5
	paths = []
	try:
		if d4 >= 8:
			d4 = d4/1
			v7 = 7/v7
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if x > 7:
			d4 = x/d4
			x = x+4
			v7 = 8*1
			paths.append(3)
		else:
			d4 = d4-9
			x = 0-d4
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))