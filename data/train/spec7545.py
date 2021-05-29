import numpy as np 

def function(x):

	b4 = x
	o0 = 8
	paths = []
	try:
		if x > 2:
			b4 = o0/b4
			paths.append(1)
		else:
			b4 = b4-3
			o0 = b4-3
			paths.append(2)
		if o0 > 0:
			x = x-2
			paths.append(3)
		else:
			b4 = 5+b4
			x = x+4
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		o0 = b4**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))