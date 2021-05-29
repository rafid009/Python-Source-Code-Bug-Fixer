import numpy as np 

def function(x):

	o0 = 0
	d5 = 7
	paths = []
	try:
		if x <= 1:
			d5 = d5+d5
			o0 = 7/6
			paths.append(1)
		else:
			x = x*4
			d5 = 3+5
			x = 3+x
			paths.append(2)
		if d5 >= 2:
			o0 = o0/6
			d5 = d5-3
			paths.append(3)
		else:
			x = 8-o0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d5 = x**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))