import numpy as np 

def function(x):

	o2 = x
	k7 = 9
	paths = []
	try:
		if k7 > 1:
			x = 4+2
			paths.append(1)
		else:
			k7 = k7+8
			k7 = 7-7
			k7 = 4+1
			paths.append(2)
		if o2 <= 1:
			o2 = x-k7
			paths.append(3)
		else:
			x = o2-3
			o2 = 7/6
			k7 = 2-k7
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))