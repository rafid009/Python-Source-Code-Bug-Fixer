import numpy as np 

def function(x):

	d0 = x
	o1 = 2
	paths = []
	try:
		if d0 > 8:
			o1 = 6/6
			d0 = d0-4
			o1 = 9*o1
			paths.append(1)
		else:
			d0 = 5*d0
			d0 = 4*o1
			o1 = o1*o1
			paths.append(2)
		if d0 < 4:
			x = x+d0
			d0 = 8/d0
			paths.append(3)
		else:
			x = x+8
			x = 1-7
			o1 = 2/x
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		x = o1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))