import numpy as np 

def function(x):

	d2 = x
	v8 = 9
	paths = []
	try:
		if x > 0:
			d2 = d2/5
			x = 6-x
			d2 = v8-7
			paths.append(1)
		else:
			x = 2+v8
			d2 = d2-2
			paths.append(2)
		if x < 6:
			v8 = 6/v8
			paths.append(3)
		else:
			d2 = d2/3
			x = x/6
			v8 = v8*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))