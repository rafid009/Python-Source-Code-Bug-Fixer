import numpy as np 

def function(x):

	d8 = x
	f0 = 5
	paths = []
	try:
		if x <= 2:
			d8 = x+9
			x = x-d8
			paths.append(1)
		else:
			x = d8+f0
			x = 8-x
			paths.append(2)
		if d8 >= 7:
			d8 = d8*f0
			x = x+5
			paths.append(3)
		else:
			f0 = 8/f0
			x = f0-x
			d8 = d8*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))