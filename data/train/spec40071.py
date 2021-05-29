import numpy as np 

def function(x):

	d0 = 5
	o6 = x
	paths = []
	try:
		if o6 <= 2:
			o6 = d0*o6
			o6 = o6/3
			paths.append(1)
		else:
			x = 7+x
			paths.append(2)
		if o6 > 0:
			d0 = d0*d0
			o6 = o6-1
			x = 2-d0
			paths.append(3)
		else:
			d0 = d0-d0
			x = o6*x
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		d0 = o6**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))