import numpy as np 

def function(x):

	k2 = 4
	o2 = x
	x = x
	paths = []
	try:
		if k2 > 4:
			k2 = k2/2
			k2 = 1*k2
			paths.append(1)
		else:
			o2 = x+o2
			paths.append(2)
		if x < 8:
			x = x-8
			x = 0-x
			x = k2/x
			paths.append(3)
		else:
			x = x-k2
			o2 = o2+x
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