import numpy as np 

def function(x):

	v0 = 6
	o6 = 4
	paths = []
	try:
		if v0 >= 1:
			v0 = 5-x
			x = x+5
			paths.append(1)
		else:
			x = x*5
			o6 = o6/5
			x = x-3
			paths.append(2)
		if o6 <= 3:
			o6 = o6+8
			x = x-v0
			o6 = x-6
			paths.append(3)
		else:
			v0 = v0-o6
			x = 8/x
			v0 = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))