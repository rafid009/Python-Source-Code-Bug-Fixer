import numpy as np 

def function(x):

	n6 = x
	f7 = x
	paths = []
	try:
		if n6 < 3:
			n6 = 6-n6
			x = x*n6
			paths.append(1)
		else:
			x = x*6
			n6 = n6/4
			x = 9+8
			paths.append(2)
		if x < 0:
			n6 = 4-n6
			f7 = f7-n6
			paths.append(3)
		else:
			n6 = n6*0
			x = x/3
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