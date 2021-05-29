import numpy as np 

def function(x):

	o4 = 8
	x0 = x
	paths = []
	try:
		if x0 < 8:
			o4 = o4*8
			o4 = o4+x
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if x > 0:
			o4 = o4*o4
			x = o4/x
			paths.append(3)
		else:
			x0 = 6+x0
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x = x0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))