import numpy as np 

def function(x):

	q1 = 8
	d0 = 2
	paths = []
	try:
		if q1 > 5:
			d0 = x/d0
			paths.append(1)
		else:
			d0 = x*x
			paths.append(2)
		if q1 < 8:
			x = 4+9
			paths.append(3)
		else:
			d0 = d0+1
			x = x+d0
			q1 = d0*q1
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