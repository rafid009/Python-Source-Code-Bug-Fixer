import numpy as np 

def function(x):

	o0 = 3
	d6 = 8
	paths = []
	try:
		if o0 < 2:
			x = 3/6
			paths.append(1)
		else:
			o0 = 5/o0
			x = d6-x
			o0 = o0-2
			paths.append(2)
		if x <= 2:
			d6 = d6+x
			x = 8/x
			x = 2*o0
			paths.append(3)
		else:
			o0 = 6/o0
			x = x/x
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		o0 = o0**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))