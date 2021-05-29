import numpy as np 

def function(x):

	d6 = 8
	o0 = x
	paths = []
	try:
		if o0 < 7:
			x = 7+x
			paths.append(1)
		else:
			x = 1/x
			d6 = d6-7
			x = 4+d6
			paths.append(2)
		if x > 3:
			o0 = d6+d6
			d6 = d6/8
			paths.append(3)
		else:
			d6 = d6-4
			x = x/8
			d6 = 5*d6
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		d6 = o0**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))