import numpy as np 

def function(x):

	r4 = x
	n6 = 8
	paths = []
	try:
		if n6 > 3:
			x = 6+8
			x = x-r4
			paths.append(1)
		else:
			x = 0+0
			n6 = 5+n6
			x = x/r4
			paths.append(2)
		if r4 <= 5:
			n6 = n6*2
			x = r4-3
			paths.append(3)
		else:
			n6 = x/n6
			n6 = n6+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))