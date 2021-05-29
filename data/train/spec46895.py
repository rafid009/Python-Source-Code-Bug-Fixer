import numpy as np 

def function(x):

	o7 = x
	d9 = x
	x = x
	paths = []
	try:
		if d9 >= 1:
			d9 = o7*1
			d9 = 8/d9
			d9 = 3*d9
			paths.append(1)
		else:
			o7 = d9/7
			o7 = 8/o7
			paths.append(2)
		if x > 8:
			o7 = o7-3
			x = o7+x
			paths.append(3)
		else:
			d9 = 3/d9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))