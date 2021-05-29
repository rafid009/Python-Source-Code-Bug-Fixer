import numpy as np 

def function(x):

	o4 = x
	b2 = 1
	paths = []
	try:
		if o4 <= 4:
			b2 = 8*4
			paths.append(1)
		else:
			x = o4*x
			b2 = 9+o4
			x = x-5
			paths.append(2)
		if o4 >= 5:
			o4 = o4*3
			paths.append(3)
		else:
			o4 = o4*8
			b2 = o4/b2
			x = x/o4
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		o4 = o4**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))