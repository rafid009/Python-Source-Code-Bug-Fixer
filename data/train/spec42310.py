import numpy as np 

def function(x):

	s4 = x
	d4 = x
	paths = []
	try:
		if s4 < 7:
			d4 = 7/d4
			d4 = 2-d4
			d4 = d4/2
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if x > 4:
			d4 = 6/s4
			paths.append(3)
		else:
			x = x-x
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