import numpy as np 

def function(x):

	z6 = x
	w4 = 3
	paths = []
	try:
		if x > 3:
			x = x/w4
			x = x*7
			paths.append(1)
		else:
			w4 = 8/w4
			paths.append(2)
		if z6 >= 7:
			w4 = x/4
			paths.append(3)
		else:
			w4 = w4*5
			w4 = x-6
			w4 = 0*4
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))