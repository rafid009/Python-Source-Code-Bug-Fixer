import numpy as np 

def function(x):

	d0 = x
	v6 = 0
	x = x
	paths = []
	try:
		if v6 <= 7:
			d0 = x+d0
			v6 = 1/d0
			paths.append(1)
		else:
			d0 = x*d0
			d0 = 5/d0
			paths.append(2)
		if v6 >= 1:
			v6 = v6*4
			x = d0-d0
			paths.append(3)
		else:
			v6 = v6-8
			v6 = 4-8
			v6 = v6-d0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d0 = x**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))