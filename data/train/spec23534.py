import numpy as np 

def function(x):

	o9 = 2
	r4 = x
	paths = []
	try:
		if o9 < 2:
			x = x/2
			r4 = 3-9
			paths.append(1)
		else:
			o9 = 3*8
			paths.append(2)
		if r4 > 4:
			r4 = r4*3
			x = r4-2
			paths.append(3)
		else:
			o9 = o9/8
			o9 = o9/x
			o9 = o9/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o9 = x**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))