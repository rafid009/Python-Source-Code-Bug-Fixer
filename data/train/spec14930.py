import numpy as np 

def function(x):

	u2 = x
	o4 = x
	paths = []
	try:
		if u2 >= 0:
			o4 = o4+8
			paths.append(1)
		else:
			o4 = 0*2
			paths.append(2)
		if o4 < 2:
			o4 = o4+u2
			paths.append(3)
		else:
			o4 = 7/8
			o4 = 8/5
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		x = o4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))