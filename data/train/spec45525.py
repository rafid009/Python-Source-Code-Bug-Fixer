import numpy as np 

def function(x):

	o5 = x
	d5 = x
	paths = []
	try:
		if o5 >= 3:
			o5 = o5+4
			x = x/8
			paths.append(1)
		else:
			o5 = x-3
			o5 = o5+0
			paths.append(2)
		if d5 >= 5:
			o5 = o5+8
			paths.append(3)
		else:
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		x = o5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))