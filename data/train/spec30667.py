import numpy as np 

def function(x):

	k6 = x
	d4 = 9
	paths = []
	try:
		if x >= 1:
			d4 = d4-d4
			d4 = 9*8
			paths.append(1)
		else:
			d4 = 0-d4
			paths.append(2)
		if d4 <= 2:
			x = 6-2
			paths.append(3)
		else:
			x = 1+x
			k6 = k6/k6
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		d4 = d4**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))