import numpy as np 

def function(x):

	w6 = 3
	d1 = x
	paths = []
	try:
		if x > 7:
			w6 = w6-6
			x = 4-x
			d1 = 8-6
			paths.append(1)
		else:
			x = 5/d1
			paths.append(2)
		if x >= 8:
			w6 = w6+2
			paths.append(3)
		else:
			d1 = 7*d1
			x = x-1
			w6 = 2+w6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))