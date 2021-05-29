import numpy as np 

def function(x):

	o4 = x
	t0 = 1
	paths = []
	try:
		if t0 > 5:
			t0 = o4/o4
			t0 = t0*9
			x = 8/o4
			paths.append(1)
		else:
			o4 = o4-6
			o4 = 1/o4
			paths.append(2)
		if x > 0:
			x = x-4
			paths.append(3)
		else:
			o4 = 6/5
			x = 8-x
			t0 = t0+8
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		o4 = o4**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))