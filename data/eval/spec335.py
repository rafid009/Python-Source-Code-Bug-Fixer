import numpy as np 

def function(x):

	d1 = x
	r0 = 5
	paths = []
	try:
		if d1 > 2:
			x = x/d1
			x = r0+x
			paths.append(1)
		else:
			d1 = 8/d1
			d1 = d1*r0
			paths.append(2)
		if x <= 5:
			d1 = d1/6
			x = 0-r0
			x = x*8
			paths.append(3)
		else:
			d1 = 5/d1
			r0 = 5-d1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))