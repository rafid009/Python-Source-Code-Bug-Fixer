import numpy as np 

def function(x):

	o4 = x
	v3 = 9
	paths = []
	try:
		if v3 >= 6:
			v3 = 4-v3
			o4 = o4+x
			paths.append(1)
		else:
			o4 = x*o4
			paths.append(2)
		if o4 <= 0:
			x = x/v3
			x = x-9
			paths.append(3)
		else:
			o4 = x/x
			v3 = 2-v3
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