import numpy as np 

def function(x):

	o5 = x
	b7 = 4
	paths = []
	try:
		if x > 7:
			x = 0-6
			paths.append(1)
		else:
			b7 = b7-1
			paths.append(2)
		if o5 > 8:
			b7 = b7-1
			paths.append(3)
		else:
			o5 = o5+8
			x = 9*x
			x = 4*x
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