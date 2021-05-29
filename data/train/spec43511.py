import numpy as np 

def function(x):

	r0 = 1
	o3 = 6
	paths = []
	try:
		if x < 1:
			o3 = o3/2
			x = 2*x
			r0 = 0-r0
			paths.append(1)
		else:
			r0 = r0-6
			r0 = o3/7
			paths.append(2)
		if o3 < 9:
			x = x*r0
			paths.append(3)
		else:
			x = x-4
			r0 = o3/r0
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