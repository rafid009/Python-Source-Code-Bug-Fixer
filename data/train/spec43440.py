import numpy as np 

def function(x):

	o2 = x
	x3 = 6
	x = 3
	paths = []
	try:
		if x < 1:
			x3 = o2+6
			o2 = 4*8
			paths.append(1)
		else:
			x3 = 6+x3
			paths.append(2)
		if x >= 0:
			o2 = o2-4
			paths.append(3)
		else:
			x = x3/x
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