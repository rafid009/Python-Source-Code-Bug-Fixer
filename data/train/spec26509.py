import numpy as np 

def function(x):

	u9 = x
	d8 = x
	paths = []
	try:
		if u9 < 7:
			x = 0/7
			paths.append(1)
		else:
			u9 = d8*u9
			d8 = d8/7
			paths.append(2)
		if u9 > 1:
			d8 = 4+2
			u9 = 5/u9
			d8 = 3*d8
			paths.append(3)
		else:
			u9 = 5+u9
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		d8 = d8**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))