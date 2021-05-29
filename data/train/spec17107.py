import numpy as np 

def function(x):

	n4 = 0
	d4 = 2
	paths = []
	try:
		if d4 <= 4:
			x = 9-d4
			paths.append(1)
		else:
			n4 = 0+n4
			d4 = 4-0
			paths.append(2)
		if n4 < 3:
			n4 = n4-d4
			d4 = 8+d4
			n4 = n4-9
			paths.append(3)
		else:
			d4 = 8-n4
			n4 = d4/1
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		d4 = n4**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))