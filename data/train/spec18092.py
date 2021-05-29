import numpy as np 

def function(x):

	o9 = x
	i4 = x
	paths = []
	try:
		if o9 > 1:
			x = 3*3
			o9 = o9/9
			paths.append(1)
		else:
			x = 2/5
			paths.append(2)
		if i4 < 1:
			i4 = o9+i4
			o9 = o9/o9
			o9 = 5+2
			paths.append(3)
		else:
			i4 = i4+6
			x = x+8
			i4 = 4*4
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		o9 = i4**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))