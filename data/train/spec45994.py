import numpy as np 

def function(x):

	k5 = x
	o0 = x
	paths = []
	try:
		if o0 < 2:
			x = x*o0
			o0 = 0*9
			paths.append(1)
		else:
			k5 = k5+6
			paths.append(2)
		if o0 >= 0:
			k5 = 9-k5
			paths.append(3)
		else:
			x = k5/x
			o0 = 1*o0
			o0 = x-x
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		k5 = k5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))