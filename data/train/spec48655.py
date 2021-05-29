import numpy as np 

def function(x):

	o6 = x
	v2 = x
	paths = []
	try:
		if o6 >= 3:
			x = 6+x
			v2 = 3/8
			paths.append(1)
		else:
			x = x+2
			paths.append(2)
		if o6 > 6:
			v2 = 4*o6
			paths.append(3)
		else:
			o6 = 9*o6
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		v2 = o6**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))