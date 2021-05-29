import numpy as np 

def function(x):

	o4 = x
	d9 = 2
	x = x
	paths = []
	try:
		if d9 < 3:
			d9 = x*0
			x = x+4
			paths.append(1)
		else:
			o4 = o4-4
			o4 = o4-2
			d9 = 0*1
			paths.append(2)
		if x > 1:
			d9 = d9-4
			o4 = o4/5
			paths.append(3)
		else:
			o4 = 5*o4
			d9 = d9*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))