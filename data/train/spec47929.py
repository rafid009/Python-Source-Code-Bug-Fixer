import numpy as np 

def function(x):

	d0 = x
	r5 = x
	paths = []
	try:
		if x < 2:
			r5 = r5*r5
			x = 3-x
			r5 = 4+r5
			paths.append(1)
		else:
			x = d0+d0
			d0 = d0/4
			paths.append(2)
		if x <= 9:
			d0 = 2+d0
			d0 = 8+d0
			paths.append(3)
		else:
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		r5 = d0**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))