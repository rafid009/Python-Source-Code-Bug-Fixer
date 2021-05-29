import numpy as np 

def function(x):

	v4 = 5
	n9 = x
	paths = []
	try:
		if x < 0:
			v4 = v4*5
			x = x+4
			n9 = 4*x
			paths.append(1)
		else:
			v4 = 6+x
			paths.append(2)
		if v4 < 4:
			x = v4*v4
			v4 = v4-6
			paths.append(3)
		else:
			n9 = 6-3
			n9 = 9*1
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