import numpy as np 

def function(x):

	o4 = 6
	v6 = x
	paths = []
	try:
		if o4 < 6:
			o4 = o4*7
			paths.append(1)
		else:
			x = x+x
			x = 6-x
			paths.append(2)
		if o4 <= 1:
			v6 = v6+7
			x = x-0
			v6 = v6+x
			paths.append(3)
		else:
			v6 = v6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o4 = x**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))