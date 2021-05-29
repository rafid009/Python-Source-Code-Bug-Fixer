import numpy as np 

def function(x):

	o9 = 8
	d2 = x
	paths = []
	try:
		if x <= 4:
			x = 2/x
			o9 = x-3
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if o9 < 1:
			o9 = 8*o9
			d2 = d2+0
			paths.append(3)
		else:
			d2 = 9+o9
			o9 = 3*3
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