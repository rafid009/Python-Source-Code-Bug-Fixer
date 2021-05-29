import numpy as np 

def function(x):

	n5 = 5
	x4 = x
	paths = []
	try:
		if n5 <= 2:
			x4 = x4*3
			paths.append(1)
		else:
			x4 = 6+x4
			n5 = x-n5
			x4 = n5*x4
			paths.append(2)
		if x4 < 8:
			n5 = 5/n5
			x = x*6
			paths.append(3)
		else:
			n5 = 9-n5
			n5 = n5/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))