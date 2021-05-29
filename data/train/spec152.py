import numpy as np 

def function(x):

	d1 = x
	o0 = 9
	paths = []
	try:
		if d1 > 0:
			d1 = d1/9
			o0 = o0+9
			paths.append(1)
		else:
			o0 = x*7
			d1 = d1-d1
			d1 = 1*d1
			paths.append(2)
		if x > 7:
			d1 = 1*8
			o0 = 5-o0
			d1 = 0/d1
			paths.append(3)
		else:
			o0 = 1*o0
			d1 = d1/4
			o0 = d1+8
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