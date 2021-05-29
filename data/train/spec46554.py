import numpy as np 

def function(x):

	d8 = 4
	o1 = x
	paths = []
	try:
		if o1 < 4:
			o1 = 7/o1
			paths.append(1)
		else:
			o1 = 8/x
			x = 0-0
			o1 = o1/6
			paths.append(2)
		if o1 > 5:
			o1 = 1+o1
			o1 = o1-x
			d8 = d8/5
			paths.append(3)
		else:
			x = 8*2
			d8 = o1-d8
			x = x-2
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		x = d8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))