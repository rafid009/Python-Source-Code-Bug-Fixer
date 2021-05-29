import numpy as np 

def function(x):

	x4 = x
	n9 = x
	paths = []
	try:
		if x4 <= 4:
			n9 = 8-x
			n9 = x4/n9
			x = 6*x
			paths.append(1)
		else:
			x = 4*x
			x4 = 8*x4
			n9 = x4+0
			paths.append(2)
		if x4 < 6:
			x4 = 0*9
			x = x/5
			paths.append(3)
		else:
			x4 = 4/1
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