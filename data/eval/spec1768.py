import numpy as np 

def function(x):

	n0 = x
	o9 = 6
	paths = []
	try:
		if n0 <= 7:
			o9 = 9+4
			o9 = 5/o9
			paths.append(1)
		else:
			x = n0-0
			o9 = x-0
			x = 7*x
			paths.append(2)
		if o9 <= 5:
			o9 = o9-5
			paths.append(3)
		else:
			x = 2*5
			o9 = 4*o9
			n0 = n0/5
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		o9 = n0**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))