import numpy as np 

def function(x):

	f4 = 5
	n6 = 3
	paths = []
	try:
		if f4 <= 9:
			n6 = n6*n6
			n6 = x+n6
			paths.append(1)
		else:
			x = f4/x
			paths.append(2)
		if f4 < 3:
			x = 6*3
			n6 = 3/n6
			n6 = 7-n6
			paths.append(3)
		else:
			f4 = 4+1
			x = x-n6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n6 = x**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))