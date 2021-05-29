import numpy as np 

def function(x):

	o7 = 4
	d7 = 3
	paths = []
	try:
		if o7 >= 3:
			d7 = d7-x
			d7 = 2*d7
			paths.append(1)
		else:
			d7 = d7+0
			o7 = 2+o7
			paths.append(2)
		if o7 >= 5:
			d7 = d7+4
			d7 = 1+5
			paths.append(3)
		else:
			o7 = o7+3
			o7 = o7*0
			o7 = 1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))