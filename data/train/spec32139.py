import numpy as np 

def function(x):

	o5 = x
	d1 = 8
	paths = []
	try:
		if d1 <= 8:
			x = x*1
			d1 = d1*d1
			paths.append(1)
		else:
			x = x-x
			o5 = 1*3
			paths.append(2)
		if d1 > 6:
			o5 = 0-o5
			o5 = o5*1
			paths.append(3)
		else:
			d1 = d1-0
			d1 = d1+6
			o5 = o5/o5
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		d1 = o5**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))