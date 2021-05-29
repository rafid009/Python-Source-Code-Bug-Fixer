import numpy as np 

def function(x):

	o5 = x
	v2 = x
	paths = []
	try:
		if x >= 9:
			x = 4-x
			x = x+x
			x = o5+v2
			paths.append(1)
		else:
			x = x*v2
			x = x-2
			paths.append(2)
		if o5 < 1:
			x = 9*o5
			paths.append(3)
		else:
			o5 = o5+9
			x = 0-x
			o5 = v2/x
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		v2 = o5**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))