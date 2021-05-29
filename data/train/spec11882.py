import numpy as np 

def function(x):

	x4 = x
	p6 = 6
	paths = []
	try:
		if x4 <= 8:
			x = x-4
			x = 9+9
			x = p6-6
			paths.append(1)
		else:
			p6 = x/p6
			paths.append(2)
		if x >= 9:
			x4 = x4*0
			paths.append(3)
		else:
			p6 = p6+8
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x = x4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))