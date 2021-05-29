import numpy as np 

def function(x):

	d0 = x
	u4 = 5
	paths = []
	try:
		if d0 <= 4:
			u4 = u4/x
			d0 = 2*d0
			paths.append(1)
		else:
			u4 = 0+u4
			d0 = u4/d0
			u4 = 5-4
			paths.append(2)
		if u4 >= 4:
			x = x+9
			u4 = u4/u4
			paths.append(3)
		else:
			x = 2*u4
			x = 1/x
			u4 = u4/4
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		d0 = u4**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))