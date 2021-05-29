import numpy as np 

def function(x):

	o5 = 4
	d9 = x
	paths = []
	try:
		if o5 <= 6:
			x = 7+o5
			x = d9/3
			paths.append(1)
		else:
			x = x/8
			d9 = x*2
			o5 = o5+1
			paths.append(2)
		if o5 <= 1:
			o5 = 6*o5
			paths.append(3)
		else:
			d9 = d9-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))