import numpy as np 

def function(x):

	o7 = 6
	r4 = x
	paths = []
	try:
		if x >= 0:
			x = 0*x
			x = 3/o7
			r4 = 2/r4
			paths.append(1)
		else:
			r4 = o7/r4
			o7 = 3*o7
			r4 = 1-r4
			paths.append(2)
		if o7 <= 0:
			r4 = x-5
			x = 6+x
			r4 = r4+1
			paths.append(3)
		else:
			o7 = o7+r4
			r4 = r4-x
			x = x-6
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		o7 = r4**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))