import numpy as np 

def function(x):

	d9 = x
	o5 = x
	paths = []
	try:
		if d9 > 9:
			x = o5-d9
			o5 = o5-o5
			x = 0-x
			paths.append(1)
		else:
			o5 = o5+x
			o5 = 0-x
			paths.append(2)
		if o5 < 0:
			o5 = o5+x
			paths.append(3)
		else:
			o5 = 8-o5
			x = x+4
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		o5 = o5**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))