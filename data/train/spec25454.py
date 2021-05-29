import numpy as np 

def function(x):

	o7 = 4
	d5 = x
	paths = []
	try:
		if o7 <= 9:
			o7 = o7*o7
			d5 = d5+4
			o7 = x-3
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if x >= 5:
			x = x-5
			paths.append(3)
		else:
			d5 = 0/9
			x = d5/8
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		d5 = o7**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))