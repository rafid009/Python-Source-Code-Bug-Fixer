import numpy as np 

def function(x):

	o6 = x
	i0 = x
	paths = []
	try:
		if i0 < 8:
			o6 = 9-8
			i0 = x/i0
			x = x+i0
			paths.append(1)
		else:
			o6 = o6*4
			paths.append(2)
		if i0 > 9:
			i0 = x/8
			i0 = 9-x
			paths.append(3)
		else:
			i0 = 8+i0
			x = x-o6
			x = x*5
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		o6 = i0**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))