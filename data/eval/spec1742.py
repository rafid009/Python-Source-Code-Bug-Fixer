import numpy as np 

def function(x):

	o5 = 2
	d1 = x
	x = x
	paths = []
	try:
		if d1 < 0:
			o5 = 0*6
			paths.append(1)
		else:
			x = x*x
			d1 = d1-0
			paths.append(2)
		if o5 > 1:
			d1 = o5*d1
			paths.append(3)
		else:
			o5 = o5-8
			d1 = o5+d1
			d1 = o5+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))