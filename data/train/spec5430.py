import numpy as np 

def function(x):

	d0 = x
	v1 = 4
	paths = []
	try:
		if x <= 6:
			x = 7-v1
			d0 = 7-8
			paths.append(1)
		else:
			v1 = v1+5
			v1 = 6+v1
			paths.append(2)
		if d0 <= 8:
			v1 = v1*4
			v1 = v1+d0
			paths.append(3)
		else:
			x = x*7
			d0 = d0*1
			d0 = v1/d0
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d0 = d0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))