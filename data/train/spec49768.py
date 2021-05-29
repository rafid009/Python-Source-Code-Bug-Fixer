import numpy as np 

def function(x):

	d7 = x
	d4 = x
	paths = []
	try:
		if x <= 7:
			x = x+4
			d4 = 9/d4
			paths.append(1)
		else:
			x = d7/5
			paths.append(2)
		if x >= 3:
			d4 = d4+5
			d7 = d7+d4
			d4 = x-1
			paths.append(3)
		else:
			d4 = d4/4
			x = x/7
			d7 = 3/2
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		d7 = d4**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))