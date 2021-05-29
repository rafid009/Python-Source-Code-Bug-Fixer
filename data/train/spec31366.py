import numpy as np 

def function(x):

	r5 = x
	d1 = 8
	paths = []
	try:
		if r5 < 7:
			x = 5/x
			r5 = r5*1
			paths.append(1)
		else:
			x = x+2
			x = 5-x
			x = 0+x
			paths.append(2)
		if r5 <= 2:
			r5 = r5-x
			x = x-0
			paths.append(3)
		else:
			x = x+6
			d1 = d1-1
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