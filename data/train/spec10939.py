import numpy as np 

def function(x):

	d5 = x
	x4 = x
	x = x
	paths = []
	try:
		if x4 >= 5:
			d5 = 7*8
			paths.append(1)
		else:
			d5 = d5+4
			x4 = 6-x4
			d5 = d5/5
			paths.append(2)
		if x4 > 0:
			x = 3-x
			d5 = 8-x4
			paths.append(3)
		else:
			x = x4*d5
			x = 3-x
			x4 = 6*0
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