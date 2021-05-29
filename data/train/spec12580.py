import numpy as np 

def function(x):

	d5 = 5
	o9 = x
	paths = []
	try:
		if d5 >= 0:
			o9 = o9/4
			o9 = 9+o9
			x = x-0
			paths.append(1)
		else:
			o9 = o9/1
			paths.append(2)
		if o9 >= 2:
			d5 = d5/o9
			paths.append(3)
		else:
			x = o9-x
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		x = o9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))