import numpy as np 

def function(x):

	w4 = 0
	k7 = 8
	x = x
	paths = []
	try:
		if k7 >= 8:
			w4 = 6+2
			paths.append(1)
		else:
			k7 = k7+k7
			k7 = k7/1
			x = w4+5
			paths.append(2)
		if x > 0:
			w4 = x-w4
			paths.append(3)
		else:
			k7 = 9/1
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))