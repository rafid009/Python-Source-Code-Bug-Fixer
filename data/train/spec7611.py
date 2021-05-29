import numpy as np 

def function(x):

	w6 = x
	n0 = x
	paths = []
	try:
		if w6 < 6:
			n0 = n0*1
			w6 = w6+7
			paths.append(1)
		else:
			x = 8/7
			n0 = x-4
			x = n0+x
			paths.append(2)
		if w6 < 9:
			w6 = w6+w6
			x = 5+4
			paths.append(3)
		else:
			n0 = w6+5
			w6 = n0+w6
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