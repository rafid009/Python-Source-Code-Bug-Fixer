import numpy as np 

def function(x):

	k4 = 8
	d2 = 0
	paths = []
	try:
		if k4 < 2:
			k4 = d2+x
			x = k4-d2
			paths.append(1)
		else:
			k4 = 6*7
			paths.append(2)
		if x > 0:
			x = x+7
			k4 = k4+8
			k4 = 6+x
			paths.append(3)
		else:
			d2 = 9-d2
			d2 = 7-k4
			x = x-4
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		k4 = d2**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))