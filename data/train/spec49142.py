import numpy as np 

def function(x):

	r7 = 2
	d6 = x
	paths = []
	try:
		if d6 < 6:
			d6 = d6*4
			x = x-x
			paths.append(1)
		else:
			x = x/d6
			x = x-7
			paths.append(2)
		if r7 > 0:
			d6 = r7+x
			d6 = r7-4
			r7 = 9-r7
			paths.append(3)
		else:
			r7 = r7/7
			r7 = 6*r7
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