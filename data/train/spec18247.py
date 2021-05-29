import numpy as np 

def function(x):

	o0 = 0
	d1 = x
	paths = []
	try:
		if o0 < 4:
			d1 = 7/d1
			paths.append(1)
		else:
			x = 9-x
			x = 0*4
			o0 = 4/o0
			paths.append(2)
		if o0 < 8:
			d1 = 0+x
			o0 = 3+o0
			o0 = o0*1
			paths.append(3)
		else:
			o0 = 2*d1
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		d1 = d1**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))