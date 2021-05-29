import numpy as np 

def function(x):

	d5 = 7
	r4 = 6
	x = x
	paths = []
	try:
		if x >= 7:
			x = 3-x
			paths.append(1)
		else:
			d5 = x+x
			d5 = d5+x
			x = x*7
			paths.append(2)
		if x >= 8:
			r4 = 8/x
			r4 = r4+6
			paths.append(3)
		else:
			d5 = d5+d5
			x = 6-3
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))