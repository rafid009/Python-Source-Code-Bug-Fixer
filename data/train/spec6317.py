import numpy as np 

def function(x):

	r0 = 8
	d0 = x
	paths = []
	try:
		if r0 <= 8:
			d0 = d0-1
			paths.append(1)
		else:
			r0 = r0+d0
			r0 = 1*r0
			r0 = 9-r0
			paths.append(2)
		if x > 7:
			d0 = 7/d0
			paths.append(3)
		else:
			d0 = d0*r0
			r0 = r0*x
			d0 = d0-3
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		r0 = r0**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))