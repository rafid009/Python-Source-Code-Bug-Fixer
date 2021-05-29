import numpy as np 

def function(x):

	o4 = 2
	d8 = x
	paths = []
	try:
		if d8 < 7:
			x = 2+x
			d8 = d8-1
			x = d8+8
			paths.append(1)
		else:
			x = 6-8
			d8 = 8+d8
			o4 = 8*o4
			paths.append(2)
		if d8 > 6:
			x = x/8
			d8 = o4/o4
			d8 = d8*3
			paths.append(3)
		else:
			d8 = d8*4
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		d8 = d8**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))