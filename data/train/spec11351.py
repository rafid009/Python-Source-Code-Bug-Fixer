import numpy as np 

def function(x):

	d9 = x
	o8 = 1
	x = 8
	paths = []
	try:
		if o8 <= 0:
			x = o8+6
			x = 9/x
			paths.append(1)
		else:
			o8 = o8+9
			o8 = 2-o8
			d9 = 1*3
			paths.append(2)
		if o8 < 7:
			d9 = o8/d9
			x = x-9
			o8 = 9*o8
			paths.append(3)
		else:
			d9 = d9+x
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		d9 = o8**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))