import numpy as np 

def function(x):

	i0 = x
	n4 = x
	paths = []
	try:
		if x > 9:
			i0 = i0-9
			paths.append(1)
		else:
			x = n4*8
			x = x-x
			paths.append(2)
		if i0 < 5:
			n4 = n4*2
			paths.append(3)
		else:
			x = 4+n4
			x = x-0
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		x = i0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))