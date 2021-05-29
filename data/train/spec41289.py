import numpy as np 

def function(x):

	k7 = x
	o4 = x
	paths = []
	try:
		if k7 >= 2:
			k7 = 3-k7
			paths.append(1)
		else:
			x = x-6
			k7 = k7+4
			paths.append(2)
		if x < 2:
			o4 = o4+8
			o4 = k7+7
			paths.append(3)
		else:
			x = x-1
			k7 = k7-6
			k7 = k7/5
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		o4 = k7**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))