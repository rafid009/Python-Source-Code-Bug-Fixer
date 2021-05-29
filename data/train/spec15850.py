import numpy as np 

def function(x):

	d6 = x
	v8 = 6
	paths = []
	try:
		if d6 < 2:
			x = x/5
			d6 = d6*d6
			v8 = x-d6
			paths.append(1)
		else:
			v8 = 9-v8
			v8 = x*1
			d6 = d6*7
			paths.append(2)
		if d6 > 0:
			d6 = 0+d6
			d6 = d6*7
			paths.append(3)
		else:
			d6 = 1/d6
			v8 = v8+v8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))